from django.contrib import admin
from django.urls import path,include
from .views import Index, PersonList, PersonCreate, PersonUpdate, PersonDelete, BillList, BillCreate, BillUpdate, BillDelete 

app_name = 'finance'

urlpatterns = [
    path('index/', Index.as_view(), name='index'),

    path('person_list/', PersonList.as_view(), name='person'),
    path('person_create/', PersonCreate.as_view(), name='person_create'),
    path('person_update/<int:pk>/', PersonUpdate.as_view(), name='person_update'),
    path('person_delete/<int:pk>/', PersonDelete.as_view(), name='person_delete'),

    path('bill_list/', BillList.as_view(), name='bill'),
    path('bill_create/', BillCreate.as_view(), name='bill_create'),
    path('bill_update/<int:pk>/', BillUpdate.as_view(), name='bill_update'),
    path('bill_delete/<int:pk>/', BillDelete.as_view(), name='bill_delete'),
]