from django.contrib import admin

from .models import DollarRate

@admin.register(DollarRate)
class DollarRateAdmin(admin.ModelAdmin):
    readonly_fields = ['rate', 'date']
