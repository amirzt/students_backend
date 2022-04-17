from django.db import models

# Create your models here.
from Lessons.models import ScheduleItem
from Users.models import CustomUser

DAYS = [
    ('شنبه', 1),
    ('یکشنبه', 2),
    ('دوشنبه', 3),
    ('سه شنبه', 4),
    ('چهارشنبه', 5),
    ('پنجشنبه', 6),
    ('جمعه', 7),
]


class CurriculumItem(models.Model):
    scheduleItem = models.ForeignKey(ScheduleItem, on_delete=models.CASCADE)
    day = models.CharField(choices=DAYS, max_length=8)
    week = models.IntegerField(null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)

