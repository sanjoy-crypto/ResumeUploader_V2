from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.utils.safestring import mark_safe

# Create your models here.

CITY = (
        ('Dhaka', 'Dhaka'),
        ('Gazipur', 'Gazipur'),
        ('Chittagong', 'Chittagong'),
        ('Khulna', 'Khulna'),
        ('Sylhet', 'Sylhet'),
        ('Rajshahi', 'Rajshahi'),
        ('Mymensingh', 'Mymensingh'),
        ('Barisal', 'Barisal'),
        ('Rangpur', 'Rangpur'),
        ('Comilla', 'Comilla'),
        ('Narayanganj', '	Narayanganj'),
        )

class Resume(models.Model):
    name = models.CharField(max_length=100)
    birth = models.DateField(auto_now=False,auto_now_add=False)
    gender = models.CharField(max_length=100)
    work = models.CharField(max_length=100)
    education = models.TextField(max_length=200)
    phone = models.PositiveIntegerField()
    email = models.EmailField(max_length=50)
    experience = models.TextField(max_length=500)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100,choices=CITY)
    zip = models.PositiveIntegerField()
    job_city = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile_pic',blank=True)
    my_file = models.FileField(upload_to='doc',blank=True)

    def __str__(self):
        return self.name
  
    def image_tag(self):
        if self.profile_image.url is not None:
            return mark_safe('<img src="{}" height="50px" />'.format(self.profile_image.url))
        else:
            return ""


    
