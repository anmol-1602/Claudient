from django.contrib import admin

# Register your models here.
from .models import doubt,reply,userMoreInfo

admin.site.register(doubt)

admin.site.register(reply)
admin.site.register(userMoreInfo)