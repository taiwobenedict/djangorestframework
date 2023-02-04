from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('api/', views.api_root),
  path('api/snippets/', views.all_snippets, name= 'all_snippets'),
  path('api/snippets/<int:pk>/', views.single_snippet),
  path('api/snippets/users/', views.all_users, name= 'all_users'),
]