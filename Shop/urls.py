from rest_framework.urls import path
from . import views

urlpatterns = [
    path('get_plans/', views.get_plans, name='get_plans'),
    path('order/', views.order, name='order'),
    path('get_orders/', views.get_orders, name='get_orders'),

]
