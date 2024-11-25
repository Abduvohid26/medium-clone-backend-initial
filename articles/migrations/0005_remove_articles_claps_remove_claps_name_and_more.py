# Generated by Django 4.2.14 on 2024-11-25 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0004_claps_articles_claps'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='claps',
        ),
        migrations.RemoveField(
            model_name='claps',
            name='name',
        ),
        migrations.AddField(
            model_name='articles',
            name='reads_count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='articles',
            name='views_count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='claps',
            name='article',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='claps', to='articles.articles'),
        ),
        migrations.AddField(
            model_name='claps',
            name='count',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='claps',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='claps_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='articles',
            name='topics',
        ),
        migrations.AddField(
            model_name='articles',
            name='topics',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='articles.topics'),
            preserve_default=False,
        ),
    ]
