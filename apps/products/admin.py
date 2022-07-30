from django.contrib import admin
from .models import Result, Group
from mptt.admin import MPTTModelAdmin
# Register your models here.

admin.site.register(Result)
admin.site.register(Group, MPTTModelAdmin) 