from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import About

@admin.register(About)
class NewAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
