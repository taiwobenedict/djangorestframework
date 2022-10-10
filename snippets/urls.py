from django.urls import path
from . import views

urlpatterns = [
  path('', views.index),
  path('api/snippets/', views.all_snippets),
  path('api/snippets/<int:pk>/', views.single_snippet),
]