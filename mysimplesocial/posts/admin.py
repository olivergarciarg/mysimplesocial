from django.contrib import admin

# Register your models here.
from . import models


# this class is to allow to edit records in the admin page
class PostInline(admin.TabularInline):
    model = models.Post


admin.site.register(models.Post)
