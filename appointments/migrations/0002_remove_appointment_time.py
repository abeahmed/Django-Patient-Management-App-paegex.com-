# Generated by Django 3.2.5 on 2021-08-06 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='time',
        ),
    ]
