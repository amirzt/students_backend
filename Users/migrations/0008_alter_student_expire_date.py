# Generated by Django 3.2.5 on 2022-04-17 06:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0007_auto_20220417_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 24, 11, 27, 6, 83820)),
        ),
    ]