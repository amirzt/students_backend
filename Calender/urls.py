from rest_framework.urls import path
from . import views


urlpatterns = [
    path('add_task', views.add_task, name='add_task'),
    path('get_task', views.get_task, name='get_task'),
    path('delete_task', views.delete_task, name='delete_task'),
    path('edit_task', views.edit_task, name='edit_task')
]