# Generated by Django 5.0.4 on 2024-04-30 14:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_fullexams_examquestionfull'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fullexams',
            name='exam_exit',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Exam Exit At'),
        ),
        migrations.AlterField(
            model_name='fullexams',
            name='finish_exam',
            field=models.DateTimeField(verbose_name='Exam Finish At'),
        ),
        migrations.AlterField(
            model_name='quickexams',
            name='exam_exit',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Exam Exit At'),
        ),
        migrations.AlterField(
            model_name='quickexams',
            name='finish_exam',
            field=models.DateTimeField(verbose_name='Exam Finish At'),
        ),
    ]
