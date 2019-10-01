from django.contrib import admin
from . import models


# this class is to allow to edit records in the admin page
class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember


admin.site.register(models.Group)
admin.site.register(models.GroupMember)
