# Generated by Django 5.1.1 on 2024-10-22 18:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kopero_auth', '0002_crewmember_average_rating'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('is_booked', models.BooleanField(default=False)),
                ('booking_number', models.CharField(blank=True, editable=False, max_length=20, unique=True)),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField(blank=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('served', 'Served'), ('canceled', 'Canceled')], default='pending', max_length=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_bookings', to='kopero_auth.client')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL)),
                ('crew_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crew_bookings', to='kopero_auth.crewmember')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_%(class)s', to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kopero_auth.client')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(null=True)),
                ('rating', models.PositiveIntegerField()),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='booking.booking')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_reviews', to='kopero_auth.client')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL)),
                ('crew_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crew_reviews', to='kopero_auth.crewmember')),
                ('modified_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_%(class)s', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='booking',
            index=models.Index(fields=['date', 'start_time', 'crew_member'], name='booking_boo_date_9ee10d_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('booking', 'client')},
        ),
    ]