# Generated by Django 3.2.5 on 2021-11-03 19:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20211104_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 19, 58, 33, 388449, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 3, 19, 58, 33, 388449, tzinfo=utc)),
        ),
    ]
