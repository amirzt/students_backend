from rest_framework.urls import path
from . import views


urlpatterns = [
    path('add_milestone', views.add_milestone, name='add_milestone'),
    path('get_milestone', views.get_milestone, name='get_milestone'),
    path('delete_milestone', views.delete_milestone, name='delete_milestone')
]