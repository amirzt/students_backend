from django.db import models

# Create your models here.
from Users.models import Grade, CustomUser

LESSON_TYPE = [
    ('عمومی', 1),
    ('اختصاصی', 2)
]


class Lesson(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    types = models.CharField(choices=LESSON_TYPE, max_length=7)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    icon = models.ImageField(upload_to='./lesson icons')


class ScheduleItem(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    time = models.IntegerField(default=0)
    question = models.IntegerField(default=0)
    detail = models.TextField(max_length=200, null=True)

