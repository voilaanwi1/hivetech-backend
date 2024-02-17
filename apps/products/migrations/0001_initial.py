# Generated by Django 4.2.7 on 2024-02-16 08:36

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Description')),
                ('price', models.FloatField(verbose_name='Price')),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='Product Image')),
                ('type', models.CharField(choices=[('male', 'male'), ('female', 'female')], max_length=50, verbose_name='Type')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_category', to='categories.category')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
