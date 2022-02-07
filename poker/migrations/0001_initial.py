# Generated by Django 3.0.3 on 2020-05-15 22:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0004_auto_20191212_1947'),
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('table', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='room', serialize=False, to='tables.Table')),
                ('action', models.CharField(default=None, max_length=15, null=True)),
                ('pot', models.PositiveSmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('user', models.OneToOneField(max_length=24, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('moneyInTable', models.PositiveSmallIntegerField()),
                ('turn', models.BooleanField(default=False)),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='poker.Room')),
            ],
        ),
    ]
