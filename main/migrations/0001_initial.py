# Generated by Django 5.0.4 on 2024-04-28 18:21

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuickExams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=150)),
                ('exam_exit', models.DateTimeField(default=datetime.datetime.now, verbose_name='Created At')),
                ('finish_exam', models.DateTimeField(verbose_name='Created At')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profiles')),
            ],
        ),
        migrations.CreateModel(
            name='ExamQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=50, verbose_name='Question')),
                ('answer1', models.CharField(max_length=200, verbose_name='Answer 1')),
                ('answer2', models.CharField(max_length=200, verbose_name='Answer 2')),
                ('answer3', models.CharField(max_length=200, verbose_name='Answer 3')),
                ('answer4', models.CharField(max_length=200, verbose_name='Answer 4')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.quickexams')),
            ],
        ),
    ]
