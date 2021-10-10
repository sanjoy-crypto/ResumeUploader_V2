from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ['name','birth','gender','work','education','phone','email','experience','locality','city','zip','job_city','image_tag','my_file']
