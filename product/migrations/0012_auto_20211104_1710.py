# Generated by Django 3.2.5 on 2021-11-04 11:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20211104_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 4, 11, 40, 46, 842483, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 4, 11, 40, 46, 842483, tzinfo=utc)),
        ),
    ]
