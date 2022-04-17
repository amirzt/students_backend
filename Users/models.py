from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from datetime import datetime, timedelta

# Create your models here.
from Users.managers import CustomUserManager

GENDER = [
    (1, 'پسر'),
    (2, 'دختر'),
    (3, 'نامشخص')
]


class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=50, null=True, blank=False)
    user_name = models.CharField(max_length=50, null=True, blank=False, unique=True)
    phone = models.CharField(max_length=11, null=False, blank=False, unique=True)
    email = models.EmailField(null=True, blank=False, unique=True)
    is_visible = models.BooleanField(default=True)
    date_joint = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    is_student = models.BooleanField(default=False)
    is_advisor = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    # def __str__(self):
    #     return self.name


class Grade(models.Model):
    title = models.CharField(max_length=30, blank=False)


class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    gender = models.CharField(choices=GENDER, default=3, max_length=4)
    expire_date = models.DateTimeField(default=datetime.now()+timedelta(days=7))

