from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


# class UserProfile(models.Model):
# 	user=models.OneToOneField(User,unique=True,related_name='profile',on_delete=models.CASCADE)
# 	dob=models.DateField()


class userMoreInfo(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	dob = models.DateField()
	choices=[(1,u'Teacher'),(2,u'Student'),]
	designation=models.CharField(max_length=10, choices=choices)
	profilephoto=models.FileField(upload_to='upload/')
    
class doubt(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	id=models.AutoField(primary_key=True)
	question=models.TextField(null=False)
	subject=models.CharField(max_length=30,null=False)
	time=models.DateTimeField(auto_now_add=True)

class reply(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	content=models.TextField()
	par_id=models.ForeignKey(doubt,on_delete=models.CASCADE)
	time=models.DateTimeField(auto_now_add=True)

class assignment(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	subject=models.CharField(max_length=30,null=False)
	time=models.DateTimeField(auto_now_add=True)
	upload=models.FileField(upload_to='upload/')
	complete=models.BooleanField(default=False)


class notice(models.Model):
	title=models.CharField(max_length=30,default="no title")
	content=models.TextField(null=True,blank=True)
	time=models.DateTimeField(auto_now_add=True)
