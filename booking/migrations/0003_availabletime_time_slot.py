# Generated by Django 5.1.1 on 2024-10-13 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='availabletime',
            name='time_slot',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]