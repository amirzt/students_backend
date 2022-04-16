from django.db import models

# Create your models here.
LESSON_TYPE=[
    ('عمومی', 1),
    ('اختصاصی', 2)
]


class Lesson(models.Model):
    title = models.CharField(max_length=30, null=False, blank=False)
    types = models.CharField(choices=LESSON_TYPE)
    grade =