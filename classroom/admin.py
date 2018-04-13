from django.contrib import admin

# Register your models here.
from .models import doubt,reply

admin.site.register(doubt)

admin.site.register(reply)
