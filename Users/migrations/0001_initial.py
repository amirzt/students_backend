# Generated by Django 3.2.5 on 2022-04-24 08:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=50, null=True)),
                ('user_name', models.CharField(max_length=50, null=True, unique=True)),
                ('phone', models.CharField(max_length=11, unique=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('date_joint', models.DateField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_advisor', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Users.customuser')),
                ('gender', models.CharField(choices=[(1, 'پسر'), (2, 'دختر'), (3, 'نامشخص')], default=3, max_length=4)),
                ('expire_date', models.DateTimeField(default=datetime.datetime(2022, 5, 1, 12, 45, 6, 4311))),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.grade')),
            ],
        ),
    ]
