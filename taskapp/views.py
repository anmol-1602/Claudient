from django.shortcuts import render


# Create your views here.

from django.shortcuts import render
from django.shortcuts import render,redirect

from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

from django.db.models import F
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm
from django.contrib.auth import update_session_auth_hash, login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from social_django.models import UserSocialAuth

from django.forms import ModelForm
from .models import usertask


from django import forms
from django.core.exceptions import ValidationError

from django.conf import settings
from django_popup_view_field.registry import registry_popup_view
from django.views.generic import TemplateView


from allauth.account.forms import SignupForm


# Create your views here.


class addtaskform(ModelForm):
	class Meta:
		model=usertask
		fields=['content','upload']

class edittaskform(forms.Form):
	newcontent=forms.CharField(max_length=300)



def home(request):
	return render(request,'taskapp/home.html')

@login_required
def profile(request):
	user=request.user;
	context={'user':user}
	return render(request,'taskapp/profile.html',context)

@login_required
def addtask(request):
	
	if request.method=='POST':
		form=addtaskform(request.POST,request.FILES)

		if form.is_valid():
			
			content=form.cleaned_data['content']
			pic=form.cleaned_data['upload']
			newtask=usertask(content=content,owner=request.user,upload=pic)
			# uid=newtask.id // GIVES NONE
			newtask.save()
			newtask.priority=newtask.id 
			newtask.save()
						#id is allotedonly after save not create *
			
			return redirect('taskapp:tasks')

		else:
			return redirect('taskapp:addtask')
	else:
		form=addtaskform()
		return render(request,'taskapp/addtask.html',{'form':form})

@login_required
def tasks(request):
	user=request.user
	
	complete=usertask.objects.filter(owner=user,complete=True).order_by('-priority')
	incomplete=usertask.objects.filter(owner=user,complete=False).order_by('-priority')
	form=edittaskform()
	context={'user':user,'complete':complete,'incomplete':incomplete,'form':form}

	return render(request,'taskapp/tasks.html',context)
	
def moveup(request,prid):
	task=usertask.objects.get(priority=prid)
	
	task2=usertask.objects.get(priority=int(prid)+1)
	temp=task2.priority
	task2.priority=task.priority
	task.priority=temp
	task.save()
	task2.save()
	return HttpResponseRedirect(reverse('taskapp:tasks'))

def movedown(request,prid):
	task=usertask.objects.get(priority=prid)
	task2=usertask.objects.get(priority=int(prid)-1)
	temp=task2.priority
	task2.priority=task.priority
	task.priority=temp
	task.save()
	task2.save()
	return HttpResponseRedirect(reverse('taskapp:tasks'))


def complete(request,taskid):
	task=usertask.objects.get(id=taskid)
	task.complete=True
	task.save()
	return HttpResponseRedirect(reverse('taskapp:tasks'))


def incomplete(request,taskid):
	task=usertask.objects.get(id=taskid)
	task.complete=False
	task.save()
	return HttpResponseRedirect(reverse('taskapp:tasks'))

def edittask(request,taskid):
	if request.method=='POST':
		form=edittaskform(request.POST)

		if form.is_valid():
			
			newcontent=form.cleaned_data['newcontent']
			task=usertask.objects.get(id=taskid)
			task.content=newcontent
			task.save()
			return redirect('taskapp:tasks')

		else:
			return redirect('taskapp:tasks')
	else:
		form=edittaskform()
		return render(request,'taskapp/tasks.html',{'form':form})
