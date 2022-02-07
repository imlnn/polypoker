# Generated by Django 2.2.1 on 2019-08-01 13:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=24, unique=True)),
                ('buyIn', models.IntegerField(validators=[django.core.validators.MinValueValidator(
                    100), django.core.validators.MaxValueValidator(100000000)])),
                ('maxNoOfPlayers', models.IntegerField(validators=[
                 django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(8)])),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('lastUsed', models.DateTimeField(auto_now_add=True))
            ],
        ),
    ]
