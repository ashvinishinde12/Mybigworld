 

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
   path('shoponline',views.webpage2,name='webpage2'),
   
    
]
