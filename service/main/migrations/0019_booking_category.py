# Generated by Django 4.1.4 on 2023-04-29 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_booking_contactno_booking_days_booking_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.categorydetails'),
        ),
    ]
