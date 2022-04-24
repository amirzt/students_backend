from django.db import models

# Create your models here.
from Users.models import CustomUser


class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField(null=False)
    description = models.CharField(null=True, max_length=150)
    send_notification = models.BooleanField(default=False)
