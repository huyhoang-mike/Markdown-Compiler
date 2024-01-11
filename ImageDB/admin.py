from django.contrib import admin
from .models import Image
# Register your models here.

# class ImageAdmin(admin.ModelAdmin):
#     readonly_fileds = ('id',)

admin.site.register(Image)