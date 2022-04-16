from django.db import models

# Create your models here.
from Users.models import Grade, CustomUser

LESSON_TYPE = [
    ('عمومی', 1),
    ('اختصاصی', 2)
]

DAYS = [
    ('شنبه', 1),
    ('یکشنبه', 2),
    ('دوشنبه', 3),
    ('سه شنبه', 4),
    ('چهارشنبه', 5),
    ('پنجشنبه', 6),
    ('جمعه', 7),
]


class Lesson(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    types = models.CharField(choices=LESSON_TYPE, max_length=7)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='./lesson icons')


class ScheduleWeek(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_date = models.DateField(null=False)


class ScheduleItem(models.Model):
    week = models.ForeignKey(ScheduleWeek, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    day = models.CharField(choices=DAYS, null=False, max_length=8)
    time = models.IntegerField(default=0)
    question = models.IntegerField(default=0)
    detail = models.TextField(max_length=200, null=True)

