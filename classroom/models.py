from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class UserProfile(models.Model):
	user=models.OneToOneField(User,unique=True,related_name='profile',on_delete=models.CASCADE)
	dob=models.DateField()

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




