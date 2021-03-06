# Generated by Django 2.2 on 2019-04-24 10:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seed_type', models.CharField(choices=[('RE', 'Rice'), ('CN', 'Cotton'), ('SM', 'Sorghum')], default='RE', max_length=2)),
                ('amount_of_seeds', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(1)])),
                ('days_online', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]
