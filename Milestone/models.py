from django.db import models

# Create your models here.
from Users.models import CustomUser

STATES = [
    (1, 'درحال انجام'),
    (2, 'موفق شده'),
    (3, 'شکست خورده'),
]


class Milestone(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=150, null=True, blank=False)
    date = models.DateTimeField(null=False)
    state = models.CharField(choices=STATES, max_length=11, default=1)
