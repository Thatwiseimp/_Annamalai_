from django.urls import path
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='inventory'),
    path('inv/', views.inv, name='inventory'),
]