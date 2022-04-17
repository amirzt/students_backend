from rest_framework.urls import path
from . import views


urlpatterns = [
    path('add_personal_plan/', views.add_personal_plan, name='add_personal_plan'),
    path('get_all_week/', views.get_all_week, name='get_all_week'),
    path('delete/', views.delete, name='delete')
    # path('get_total_week/', views.get_total_week, name='get_total_total'),
]