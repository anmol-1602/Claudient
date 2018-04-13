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
from .models import UserProfile,doubt,reply

# Create your views here. 


class SignupForm(UserCreationForm):
	dob=forms.DateField()

	def signup(self, request, user):
		up=user.profile
		up.dob=self.cleaned_data['dob']
		user.save()
		up.save()

	class Meta:
		model=UserProfile
		fields=('dob', )



class adddoubtform(forms.ModelForm):

	class Meta:
		model=doubt
		fields=['question','subject',]
	


class replyform(forms.ModelForm):

	class Meta:
		model=reply
		fields=['content']
		labels={"content" : "reply"}


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
	return render(request,'classroom/alldoubts.html',{'form':form, 'doubts':doubts})


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
			newreply=form.save(commit=False)
			newreply.user=request.user
			newreply.par_id=doubt.objects.get(id=doubt_id)
			newreply.save()	
			# question=form.cleaned_data['question']
			# subject=form.cleaned_data['subject']
			# newdoubt=doubt(subject=subject,user=request.user,question=question)
			# newdoubt.save()
			return redirect(reverse('classroom:alldoubts'))
		else:
			doubts=doubts.objects.all()	
			return render(request,'classroom/alldoubts.html',{'form':form, 'doubts':doubts})
	else:
		form=replyform()
		doubts=doubts.objects.all()	
		return render(request,'classroom/alldoubts.html',{'form':form,'doubts':doubts})