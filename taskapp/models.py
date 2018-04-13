

from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db import models
# from django.dispatch import receiver
# from django.db.models.signals import post_save

from django.conf import settings
import datetime
# from .utils import new_key,totp
import binascii
import time
from django.conf import settings
from django.db import models

# Create your models here.




class usertask(models.Model):				#migrate gives error sometimes due to migrations file not match jaise agar makemigration kiya but migrate nhi
											# aise ma migrations file delete karke firse makemigratns and migrate karo

	id=models.AutoField(primary_key=True)
	content=models.CharField(max_length=300)
	pub_date=models.DateTimeField('date created',auto_now_add=True)
	priority=models.IntegerField(default=0)
	complete=models.BooleanField(default=False)
	upload=models.FileField(upload_to='upload/')
	owner = models.ForeignKey(User,on_delete=models.CASCADE)