from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'pizza_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('pizza/<int:id>/', views.pizza, name='pizza')
]