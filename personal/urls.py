from django.contrib import admin
from django.urls import path
from personal import views

urlpatterns = [
    
    path('',views.index,name='personal')
]