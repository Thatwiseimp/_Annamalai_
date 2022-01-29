from django.urls import path
from . import views

urlpatterns = [
    path('inv/', views.inv, name='inventory'),
    path('',views.index, name='index'),
    path('<int:cust_id>/',views.profile, name='profile'),
    path('add/',views.add_customer,name='add'),
    path('add/thanks/',views.thanks)
]
