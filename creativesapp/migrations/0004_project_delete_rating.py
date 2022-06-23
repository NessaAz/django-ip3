# Generated by Django 4.0.5 on 2022-06-16 18:10

import cloudinary.models
import datetime
import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('creativesapp', '0003_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('score', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.DeleteModel(
            name='Rating',
        ),
    ]
