# Generated by Django 4.2.14 on 2024-09-03 09:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='brith_year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2024)]),
        ),
        migrations.AddConstraint(
            model_name='customuser',
            constraint=models.CheckConstraint(check=models.Q(('brith_year__gt', 1900), ('brith_year__lt', 2024)), name='check_brith_year_range'),
        ),
    ]
