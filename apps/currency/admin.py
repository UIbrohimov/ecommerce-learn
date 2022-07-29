from django.contrib import admin
from .models import DollarRate
# Register your models here.

@admin.register(DollarRate)

class DollarRateAdmin(admin.ModelAdmin):
    readonly_fields = ['rate', 'date']