 
from distutils.command.upload import upload
from django.db import models


class members(models.Model):
   fruits= models.CharField(max_length=255)
   vegitable =models.CharField(max_length=255)

class productdetails(models.Model):
   product_img=models.ImageField(upload_to = 'myimages/', null=True, blank=True)
   product_title=models.CharField(max_length=200)
   product_category=models.TextField(max_length=255)
   

class imagedeatails(models.Model):
   icon_image=models.ImageField(upload_to='myimages/', null=True, blank=True)
