# Generated by Django 5.1.1 on 2024-10-16 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kopero_auth', '0007_remove_user_unique_username_email_alter_user_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='picture',
        ),
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]