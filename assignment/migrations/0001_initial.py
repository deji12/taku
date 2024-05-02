# Generated by Django 5.0.4 on 2024-04-29 12:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment_date', models.DateField()),
                ('lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.employee')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
        ),
    ]