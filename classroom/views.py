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
from .models import doubt,reply,assignment,notice,userMoreInfo
from .forms import addassignmentform,userMoreInfoForm, adddoubtform,replyform,addnotice
from allauth.account.adapter import DefaultAccountAdapter

# from django.core.cache import cache
# cache.set('noofdoubts', 0)
# cache.set('noofreplies', 0)

# Create your views here. 



def index(request):
	notices=notice.objects.all()
	return render(request,'classroom/index.html',{'notices':notices})


@login_required
def profile(request):
	return render(request,'classroom/profile.html')

@login_required
def newdoubt(request):
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
			return render(request,'classroom/newdoubt.html',{'form':form})
	else:
		form=adddoubtform()
		return render(request,'classroom/newdoubtdoubt.html',{'form':form})

@login_required
def alldoubts(request):
	form=replyform(request.POST)
	doubts=doubt.objects.all()
	noofdoubts=doubt.objects.count()
	noofreplies=reply.objects.count()
	user=request.user
	return render(request,'classroom/alldoubts.html',{'form':form, 'doubts':doubts,'noofdoubts':noofdoubts,'noofreplies':noofreplies,'user':user})


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



def allnotices(request):
	notices=notice.objects.all().order_by('-time')
	if request.method=='POST':
		form=addnotice(request.POST)
		
		if form.is_valid():			
			content=form.cleaned_data['content']
			title=form.cleaned_data['title']
			newnotice=notice(content=content,title=title)
			newnotice.save()
			return redirect(reverse('classroom:allnotices'))
		else:
			return redirect(reverse('classroom:allnotices'))
	else:
		form=addnotice()
		return render(request,'classroom/allnotices.html',{'form':form,'notices':notices})

def moreuserinfo(request):

	if request.method=='POST':
		form=userMoreInfoForm(request.POST,request.FILES)
		if form.is_valid():
			dob=form.cleaned_data['dob']
			designation=form.cleaned_data['designation']
			# pic=form.cleaned_data['uprofilepic']
			user=request.user
			newuserinfo=userMoreInfo(dob=dob,designation=designation,user=user)
			newuserinfo.save()
						
			return render(request,'classroom/profile.html')
		else:
			return render(request,'classroom/moreuserinfo.html',{'form':form})
	else:
		form=userMoreInfoForm()
		return render(request,'classroom/moreuserinfo.html',{'form':form})