# Generated by Django 4.2.1 on 2023-05-21 10:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee_app', '0014_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='course',
            field=models.ForeignKey(limit_choices_to={'isactive': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='Employee_app.course', verbose_name='Course:'),
        ),
        migrations.AlterField(
            model_name='batch',
            name='trainer',
            field=models.ForeignKey(limit_choices_to={'groups__name': 'Faculty', 'is_active': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainer', to=settings.AUTH_USER_MODEL, verbose_name='Trainer'),
        ),
    ]