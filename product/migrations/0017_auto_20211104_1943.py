# Generated by Django 3.2.5 on 2021-11-04 14:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0016_auto_20211104_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 4, 14, 13, 58, 206341, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 4, 14, 13, 58, 206341, tzinfo=utc)),
        ),
    ]