# Generated by Django 3.2.5 on 2022-04-20 05:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_alter_student_expire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 27, 9, 53, 39, 28306)),
        ),
    ]
