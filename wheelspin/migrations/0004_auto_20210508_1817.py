# Generated by Django 3.2.2 on 2021-05-08 12:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wheelspin', '0003_rooms_showed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='showed',
        ),
        migrations.AlterField(
            model_name='rooms',
            name='users_m',
            field=models.ManyToManyField(related_name='user_m', to=settings.AUTH_USER_MODEL),
        ),
    ]
