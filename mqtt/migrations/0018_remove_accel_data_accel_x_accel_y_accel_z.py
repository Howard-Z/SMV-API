# Generated by Django 4.2.7 on 2025-02-11 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mqtt', '0017_accel_blinker_gyro_x_gyro_y_gyro_z_magnetometer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accel',
            name='data',
        ),
        migrations.AddField(
            model_name='accel',
            name='x',
            field=models.DecimalField(blank=0, decimal_places=3, default=0, max_digits=6, null=0),
        ),
        migrations.AddField(
            model_name='accel',
            name='y',
            field=models.DecimalField(blank=0, decimal_places=3, default=0, max_digits=6, null=0),
        ),
        migrations.AddField(
            model_name='accel',
            name='z',
            field=models.DecimalField(blank=0, decimal_places=3, default=0, max_digits=6, null=0),
        ),
    ]
