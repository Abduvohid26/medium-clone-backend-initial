# Generated by Django 4.2.14 on 2024-11-25 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_alter_article_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-created_at'], 'verbose_name': 'Article', 'verbose_name_plural': 'Articles'},
        ),
        migrations.AlterModelOptions(
            name='claps',
            options={'ordering': ['-count'], 'verbose_name': 'Clap', 'verbose_name_plural': 'Claps'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['name'], 'verbose_name': 'Topic', 'verbose_name_plural': 'Topics'},
        ),
        migrations.AlterModelTable(
            name='claps',
            table='clap',
        ),
        migrations.AlterModelTable(
            name='topic',
            table='topic',
        ),
    ]
