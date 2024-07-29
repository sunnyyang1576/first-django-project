from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.blog_list, name='blog_list'),
    path('blogs/create/', views.blog_create, name='blog_create'),
    path('blogs/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('authors/<int:author_id>/', views.author_detail, name='author_detail'),
]