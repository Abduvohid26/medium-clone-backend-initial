# Generated by Django 4.2.14 on 2024-08-27 09:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['-date_joined'], 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterModelTable(
            name='customuser',
            table='user',
        ),
    ]
