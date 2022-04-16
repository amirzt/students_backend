from django.db import models


# Create your models here.
from Users.models import CustomUser


class Plan(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(max_length=250)
    period = models.IntegerField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    available = models.BooleanField(default=True)


class Order(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField()
    state = models.BooleanField(default=False)
    tracking_code = models.CharField(blank=False)
