from rest_framework.urls import path
from . import views

urlpatterns = [
    path('create_search_accout/', views.create_account, name='create_account'),
    path('delete_search_account/', views.delete_account, name='delete_account'),
    path('find_match/', views.find_match, name='find_match'),
    path('send_request/', views.send_request, name='send_request'),
    path('get_my_requests/', views.get_my_requests, name='get_my_requests'),
    path('get_sent_requests/', views.get_sent_requests, name='get_sent_requests'),
    path('interact_request', views.interact_request, name='interact_request')
]