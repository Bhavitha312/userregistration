from django.urls import path 
from app2 import views

urlpatterns=[
    path('display',views.display,name=''),
    path('details',views.details,name='')
]