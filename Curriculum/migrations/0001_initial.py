# Generated by Django 3.2.5 on 2022-04-16 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Lessons', '0004_auto_20220416_1410'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurriculumItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('شنبه', 1), ('یکشنبه', 2), ('دوشنبه', 3), ('سه شنبه', 4), ('چهارشنبه', 5), ('پنجشنبه', 6), ('جمعه', 7)], max_length=8)),
                ('week', models.IntegerField()),
                ('scheduleItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lessons.scheduleitem')),
            ],
        ),
    ]
