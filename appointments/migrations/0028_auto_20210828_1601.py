# Generated by Django 2.2.24 on 2021-08-28 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('appointments', '0027_auto_20210828_1551'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='appointment',
        ),
        migrations.AddField(
            model_name='department',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
