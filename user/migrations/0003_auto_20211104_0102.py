# Generated by Django 3.2.5 on 2021-11-03 19:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20211104_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 19, 32, 1, 280220, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 19, 32, 1, 280220, tzinfo=utc)),
        ),
    ]
