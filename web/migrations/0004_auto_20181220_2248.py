# Generated by Django 2.0 on 2018-12-20 16:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20181220_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='production',
            name='production_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
