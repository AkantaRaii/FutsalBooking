# Generated by Django 5.0.6 on 2024-07-29 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='futsal_court',
            name='futsal_name',
            field=models.CharField(max_length=10),
        ),
    ]
