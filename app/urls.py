from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path('',views.loginpage,name='loginpage'),
     path('land',views.land,name='land'),
     path('purchase',views.purchase,name='purchase'),
     path('loginfun',views.loginfun,name='loginfun'),
     path('logout',views.logout,name='logout'),
]