# Generated by Django 5.0.4 on 2024-04-29 23:39

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='assessment_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
