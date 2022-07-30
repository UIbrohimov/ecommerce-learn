from django.contrib import admin
from .models import Result, Group
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
# Register your models here.

admin.site.register(Result)

@admin.register(Group)
class GroupAdmin(DraggableMPTTAdmin):
    # custom options what you want
    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ('name',)}