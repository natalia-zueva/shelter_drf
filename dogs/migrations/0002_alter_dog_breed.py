# Generated by Django 5.0.2 on 2024-02-13 07:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='breed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dogs.breed', verbose_name='Порода'),
        ),
    ]