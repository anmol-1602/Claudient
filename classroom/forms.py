

from django import forms
from .models import doubt,reply,assignment,notice,userMoreInfo
from datetime import datetime
# from django.db import models
# from django.forms import ModelForm


date_range = 50    
this_year = datetime.now().year

# class SignupForm(forms.ModelForm):
#     dob = forms.DateField(label='Date of Birth',widget=forms.SelectDateWidget(years=range(this_year - date_range, this_year + date_range)))
#     designation=forms.ChoiceField(choices=[
#     	(1,u'Teacher'),
#     	(2,u'student'),])

#     def signup(self, request, user):
#         user.dob = self.cleaned_data['dob']
#         user.designation = self.cleaned_data['designation']
#         user.save()

#     class Meta:
#         model = UserProfile
#         fields=['dob']


class userMoreInfoForm(forms.Form):

    dob=forms.DateField(label='Date of Birth',widget=forms.SelectDateWidget(years=range(this_year - date_range, this_year + date_range)))
    designation=forms.ChoiceField(choices=[
      (1,u'Teacher'),
      (2,u'student'),])



         

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

class addnotice(forms.ModelForm):

    class Meta:
        model=notice
        fields=['title','content']
        