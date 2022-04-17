from rest_framework.urls import path
from . import views


urlpatterns = [
    path('add_curriculum/', views.add_curriculum, name='add_curriculum'),
    path('get_all_week/', views.get_all_week, name='get_all_week'),
    # path('get_total_week/', views.get_total_week, name='get_total_total'),
]