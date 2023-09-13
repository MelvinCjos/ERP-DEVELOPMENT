# Generated by Django 4.2.1 on 2023-05-21 10:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee_app', '0010_delete_batches'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cource',
            name='cource_name',
            field=models.CharField(max_length=255, verbose_name='Course:'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=200, unique=True)),
                ('coursecode', models.CharField(max_length=200, null=True, unique=True)),
                ('trainers', models.ManyToManyField(blank=True, limit_choices_to={'groups__name': 'Faculty', 'is_active': True}, related_name='UserTrainers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Course',
            },
        ),
    ]
