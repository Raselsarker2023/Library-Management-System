from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('add/', views.add_category, name='add_category'),
    path('category/<slug:category_slug>/', views.category_wise_post, name='category_wise_post'),
]
