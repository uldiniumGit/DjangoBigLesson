# Generated by Django 4.1.6 on 2023-04-03 12:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0017_client_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='create',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
