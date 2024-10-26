# Generated by Django 5.1.1 on 2024-10-26 03:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('booking', '0001_initial'),
        ('kopero_auth', '0001_initial'),
        ('services', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_bookings', to='kopero_auth.client'),
        ),
        migrations.AddField(
            model_name='booking',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='booking',
            name='crew',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crew_bookings', to='kopero_auth.crewmember'),
        ),
        migrations.AddField(
            model_name='booking',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_%(class)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='booking',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service'),
        ),
        migrations.AddField(
            model_name='review',
            name='booking',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='booking.booking'),
        ),
        migrations.AddField(
            model_name='review',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_reviews', to='kopero_auth.client'),
        ),
        migrations.AddField(
            model_name='review',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_%(class)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='crew_member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crew_reviews', to='kopero_auth.crewmember'),
        ),
        migrations.AddField(
            model_name='review',
            name='modified_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modified_%(class)s', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddIndex(
            model_name='booking',
            index=models.Index(fields=['date', 'time', 'crew'], name='booking_boo_date_9fd438_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('booking', 'client')},
        ),
    ]