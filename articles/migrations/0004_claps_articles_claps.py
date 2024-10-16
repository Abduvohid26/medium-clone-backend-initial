# Generated by Django 4.2.14 on 2024-10-11 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articles_author_articles_topics_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Claps',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='articles',
            name='claps',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.claps'),
        ),
    ]
