from django.contrib import admin

# Register your models here.
from Lessons.models import Lesson, ScheduleItem

admin.site.register(Lesson)
admin.site.register(ScheduleItem)
