# Generated by Django 3.2.5 on 2022-04-16 07:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0004_alter_student_expire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='expire_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 23, 12, 25, 17, 912417)),
        ),
    ]
