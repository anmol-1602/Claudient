
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

from django.contrib.admin.widgets import AdminDateWidget

from datetime import datetime


date_range = 50    
this_year = datetime.now().year

class SignupForm(forms.Form):
    dob = forms.DateField(label='Date of Birth',widget=forms.SelectDateWidget(years=range(this_year - date_range, this_year + date_range)))
    designation=forms.ChoiceField(choices=[
    	(1,u'Teacher'),
    	(2,u'student'),])

    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
       
        user.save()