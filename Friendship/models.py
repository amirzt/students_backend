from django.db import models


# Create your models here.
from Lessons.models import Lesson
from Users.models import Grade

GENDER = [
    (1, 'پسر'),
    (2, 'دختر')
]


class SearchAccount(models.Model):
    gender = models.CharField(choices=GENDER, max_length=4)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)


class Subjects(models.Model):
    search_account = models.ForeignKey(SearchAccount, on_delete=models.CASCADE)
    title = models.CharField(null=False, max_length=30)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

