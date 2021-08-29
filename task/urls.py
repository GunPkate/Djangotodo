from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', Home,name='home-page'), #localhost:8000
    path('contact/', Contact,name='contact-page'), #localhost:8000/contact
    path('about/',About,name='about-page'), #localhost:8000/about
    path('addproject/',AddProject,name='addproject-page'), 
    path('addtask/',AddTask,name='addtask-page'), 
]