"""Defines URL patterns for learning_logs."""
from django.urls import path
from . import views


app_name = 'learning_logs'

urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topic/<int:id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:id>/', views.edit_entry, name='edit_entry'),
    path('delete_entry/<int:id>/', views.delete_entry, name='delete_entry'),
    path('delete_topic/<int:id>/', views.delete_topic, name='delete_topic'),
]
