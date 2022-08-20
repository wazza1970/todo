# Generated by Django 4.0.5 on 2022-08-19 03:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_todo_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.CharField(default=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateField(default=datetime.date(2022, 8, 19)),
        ),
    ]
