from django.contrib import admin
# Register your models here.
from .models import Plan, Order

admin.site.register(Plan)
admin.site.register(Order)