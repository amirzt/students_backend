from django.contrib import admin
# Register your models here.
from .models import SearchAccount, Subjects, Request

admin.site.register(SearchAccount)
admin.site.register(Subjects)
admin.site.register(Request)
