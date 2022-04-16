from rest_framework.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('change_info/', views.change_info, name='change_info'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('get_info/', views.get_info, name='view_account'),
    path('change_password/', views.change_password, name='change_password')

]