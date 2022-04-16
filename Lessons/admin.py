from django.contrib import admin

# Register your models here.
from Lessons.models import Lesson, ScheduleWeek, ScheduleItem

admin.site.register(Lesson)
admin.site.register(ScheduleWeek)
admin.site.register(ScheduleItem)
