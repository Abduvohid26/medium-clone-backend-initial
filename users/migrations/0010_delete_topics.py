# Generated by Django 4.2.14 on 2024-09-24 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_topics'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Topics',
        ),
    ]