# Generated by Django 3.2.5 on 2021-11-03 19:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20211104_0113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 19, 54, 58, 364613, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 19, 54, 58, 364613, tzinfo=utc)),
        ),
    ]