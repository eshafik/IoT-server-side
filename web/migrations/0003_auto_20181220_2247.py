# Generated by Django 2.0 on 2018-12-20 16:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20181220_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='production_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 20, 16, 47, 23, 227536, tzinfo=utc)),
        ),
    ]
