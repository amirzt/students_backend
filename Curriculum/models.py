
from django.db import models
from Lessons.models import ScheduleItem
from Users.models import CustomUser

DAYS = [
    (1, 'شنبه'),
    (2, 'یکشنبه'),
    (3, 'دوشنبه'),
    (4, 'سه شنبه'),
    (5, 'چهارشنبه'),
    (6, 'پنجشنبه'),
    (7, 'جمعه'),
]


class CurriculumItem(models.Model):
    scheduleItem = models.ForeignKey(ScheduleItem, on_delete=models.CASCADE)
    day = models.CharField(choices=DAYS, max_length=8, null=False)
    week = models.IntegerField(null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)

