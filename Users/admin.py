from django.contrib import admin

# Register your models here.
from Users.models import CustomUser, Student

admin.site.register(CustomUser)
admin.site.register(Student)

