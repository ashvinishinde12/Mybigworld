 
 
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import members
 

 
def index(request):
  imagedata =members.objects.all()
 
  data={
    'imagedata1':imagedata
  }
   
  return render(request,'myhome.html',data)
   
def webpage2(request):
  return render(request,'shoponline.html')
 
 