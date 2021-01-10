from django.urls import path, include
from . import views

app_name = 'blogpost'

urlpatterns = [
    path('', views.index, name='index'),
    path('new_post/', views.new_post, name='new_post'),
    path('post/<int:id>', views.post, name='post'),
    path('edit_post/<int:id>', views.edit_post, name='edit_post'),
    path('delete_post/<int:id>', views.delete_post, name='delete_post'),
]