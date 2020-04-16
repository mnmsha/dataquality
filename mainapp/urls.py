
from django.contrib import admin
from django.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.dataquality_new, name='dataquality_new'),
    path('post_list/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail,  name='post_detail'),
]
