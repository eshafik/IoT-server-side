# Generated by Django 2.0 on 2018-12-18 09:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_no', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production_size', models.IntegerField()),
                ('production_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('line', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='production', to='web.Line')),
            ],
        ),
    ]