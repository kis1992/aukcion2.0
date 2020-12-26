from django.contrib import admin
from .models import BaseUser as Account

# Register your models here.

admin.site.register(Account)