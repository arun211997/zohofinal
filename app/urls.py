from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('',views.land,name='land'),
      path('purchase',views.purchase,name='purchase'),
]