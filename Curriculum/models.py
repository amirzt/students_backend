
from django.db import models
from Lessons.models import ScheduleItem
from Users.models import CustomUser


class CurriculumItem(models.Model):
    scheduleItem = models.ForeignKey(ScheduleItem, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    date = models.DateTimeField(null=False, blank=False)

