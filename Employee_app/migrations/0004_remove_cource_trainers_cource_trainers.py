# Generated by Django 4.2.1 on 2023-05-19 09:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee_app', '0003_remove_cource_trainers_cource_trainers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cource',
            name='trainers',
        ),
        migrations.AddField(
            model_name='cource',
            name='trainers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
