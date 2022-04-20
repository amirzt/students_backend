from django.db import models


# Create your models here.
from Lessons.models import Lesson
from Users.models import Grade, CustomUser

GENDER = [
    (1, 'پسر'),
    (2, 'دختر')
]

REQUEST_STATES = [
    (1, 'accepted'),
    (2, 'in progress'),
    (3, 'rejected')
]


class SearchAccount(models.Model):
    gender = models.CharField(choices=GENDER, max_length=4)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, unique=True)


class Subjects(models.Model):
    search_account = models.ForeignKey(SearchAccount, on_delete=models.CASCADE)
    description = models.CharField(null=False, max_length=30)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)


class Request(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='receiver')
    state = models.CharField(choices=REQUEST_STATES, max_length=11, default=2)
    created_time = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)

