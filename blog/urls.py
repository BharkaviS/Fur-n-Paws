"""Fur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from users import views as users_views
from blog import views as blog_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',blog_views.blog_post_list_view,name='blog'),
    path('userposts/',blog_views.blog_post_list_user_view,name='user-posts'),
    path('seller/',blog_views.seller,name='seller'),
    path('<str:slug>/',blog_views.blog_post_detail_view,name='blog-detail'),
    path('<str:slug>/update/',blog_views. blog_post_update_view,name='blog-update'),
    #path('<str:slug>/update/',blog_views.PostUpdateView,name='blog-update'),
    path('<str:slug>/delete/',blog_views.blog_post_delete_view,name='blog-delete'),
    path('contact',blog_views.contact_page,name='contact'),
    path('buyer',blog_views.loginbuyer,name='buyer'),
   
]
