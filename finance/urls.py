from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('persons', views.get_person, name='get_all_person'),
    path('bills', views.get_bill, name='get_all_bill'),
]