# Generated by Django 4.1.4 on 2023-04-28 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_vendorregistration_usertype'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendorregistration',
            name='email',
        ),
        migrations.RemoveField(
            model_name='vendorregistration',
            name='password',
        ),
        migrations.RemoveField(
            model_name='vendorregistration',
            name='username',
        ),
    ]