from django.contrib import admin
from .models import Product, Category
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ('title',)}

@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ('name',)}