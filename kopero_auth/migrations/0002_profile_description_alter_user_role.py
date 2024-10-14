# Generated by Django 5.1.1 on 2024-10-13 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kopero_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('photographer', 'Photographer'), ('Regular', 'regular'), ('Operations Admin', 'Operations Admin')], default='Regular', help_text='Designates the role of the user in the system - For Authorization', max_length=20, verbose_name='user role'),
        ),
    ]