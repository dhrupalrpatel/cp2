# Generated by Django 4.1.4 on 2023-04-16 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_category_slug_remove_categorydetails_slug_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagetable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(default='', upload_to='images/')),
                ('image2', models.ImageField(default='', upload_to='images/')),
                ('image3', models.ImageField(default='', upload_to='images/')),
                ('image4', models.ImageField(default='', upload_to='images/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categorydetails')),
            ],
        ),
    ]
