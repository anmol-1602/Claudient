from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ModelForm
from .models import UserProfile,doubt,reply,assignment

# from django.core.cache import cache
# cache.set('noofdoubts', 0)
# cache.set('noofreplies', 0)


# Create your views here. 


# class SignupForm(UserCreationForm):
# 	dob=forms.DateField()

# 	def signup(self, request, user):
# 		up=user.profile
# 		up.dob=self.cleaned_data['dob']
# 		user.save()
# 		up.save()

# 	class Meta:
# 		model=UserProfile
# 		fields=('dob', )

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='Voornaam')
    
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
       
        user.save()


class adddoubtform(forms.ModelForm):

	class Meta:
		model=doubt
		fields=['question','subject',]
	


class replyform(forms.ModelForm):

	class Meta:
		model=reply
		fields=['content']
		labels={"content" : "reply"}

class addassignmentform(forms.ModelForm):

	class Meta:
		model=assignment
		fields=['subject','upload']


def index(request):
	return render(request,'classroom/index.html')

def signup(request):
	if request.method=='POST':
		form=SignupForm(request.POST)
		if form.is_valid():
			user=form.save()
			user.save()
			username=form.cleaned_data.get('username')
			raw_password=form.cleaned_data.get('password1')
			login(request,user)
			return HttpResponseRedirect(reverse('classroom:index'))
		else:
			return render(request,'classroom/signup.html',{'form':form})
	else:
		form=SignupForm()
		return render(request,'classroom/signup.html',{'form':form})

@login_required
def profile(request):
	return render(request,'classroom/profile.html')

@login_required
def doubts(request):
	if request.method=='POST':
		form=adddoubtform(request.POST)
		if form.is_valid():
			#cache.incr('noofdoubts')
			newdoubt=form.save(commit=False)
			newdoubt.user=request.user
			newdoubt.save()	
			
			# question=form.cleaned_data['question']
			# subject=form.cleaned_data['subject']
			# newdoubt=doubt(subject=subject,user=request.user,question=question)
			# newdoubt.save()
						
			return redirect(reverse('classroom:alldoubts'))
		else:
			return render(request,'classroom/doubts.html',{'form':form})
	else:
		form=adddoubtform()
		return render(request,'classroom/doubts.html',{'form':form})

	# form=adddoubtform()
	# doubts=doubt.objects.all()
	# return render(request,'classroom/doubts.html',{'form':form,'doubts':doubts})
@login_required
def alldoubts(request):
	form=replyform(request.POST)
	doubts=doubt.objects.all()
	noofdoubts=doubt.objects.count()
	noofreplies=reply.objects.count()
	user=request.user
	return render(request,'classroom/alldoubts.html',{'form':form, 'doubts':doubts,'noofdoubts':noofdoubts,'noofreplies':noofreplies,'user':user})


def commenttry(request):
	if request.method=='POST':
		form=commentform(request.POST)
		if form.is_valid():
			newcomm=form.save(commit=False)
			newcomm.user=request.user
			newcomm.save()	
			# question=form.cleaned_data['question']
			# subject=form.cleaned_data['subject']
			# newdoubt=doubt(subject=subject,user=request.user,question=question)
			# newdoubt.save()
						
			return redirect(reverse('classroom:profile'))
		else:
			return render(request,'classroom/commenttry.html',{'form':form})
	else:
		form=commentform()
		return render(request,'classroom/commenttry.html',{'form':form})

def allcomments(request):
	comments=doubt.objects.all()
	form=replyform()
	return render(request,'classroom/allcomments.html',{'comments':comments,'form':form})


def postreply(request,doubt_id):
	if request.method=='POST':
		form=replyform(request.POST)
		if form.is_valid():
			#cache.incr('noofreplies')
			newreply=form.save(commit=False)
			newreply.user=request.user
			newreply.par_id=doubt.objects.get(id=doubt_id)
			newreply.save()	
			# question=form.cleaned_data['question']
			# subject=form.cleaned_data['subject']
			# newdoubt=doubt(subject=subject,user=request.user,question=question)
			# newdoubt.save()
			return HttpResponse(' ')
		else:
			doubts=doubts.objects.all()	
			return render(request,'classroom/alldoubts.html',{'form':form, 'doubts':doubts})
	else:
		form=replyform()
		doubts=doubts.objects.all()	
		return render(request,'classroom/alldoubts.html',{'form':form,'doubts':doubts})



def allassignments(request):
	assignments=assignment.objects.all()
	return render(request,'classroom/allassignments.html',{'assignments':assignments})

def addassignment(request):
	user=request.user
	
	if request.method=='POST':
		form=addassignmentform(request.POST,request.FILES)

		if form.is_valid():
			
			subject=form.cleaned_data['subject']
			pic=form.cleaned_data['upload']
			newassignment=assignment(subject=subject,user=request.user,upload=pic)
			newassignment.save()
			
			return redirect(reverse('classroom:allassignments'))

		else:
			return redirect(reverse('classroom:addassignment'))
	else:
		form=addassignmentform()
		return render(request,'classroom/addassignment.html',{'form':form})