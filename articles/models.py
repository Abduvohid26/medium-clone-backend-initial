from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

class Topic(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = "topic"  # Jadval nomi
        verbose_name = "Topic"  # Modelning inson o'qiy oladigan nomi
        verbose_name_plural = "Topics"  # Ko‘plik shakli
        ordering = ["name"]  # `name` bo'yicha tartiblanadi


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topics = models.ManyToManyField(Topic)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    content = models.TextField()
    status = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='articles/thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField()
    reads_count = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {self.status}'

    class Meta:
        db_table = "article"  # Jadval nomi
        verbose_name = "Article"  # Modelning inson o'qiy oladigan nomi
        verbose_name_plural = "Articles"  # Ko‘plik shakli
        ordering = ["-created_at"]  # Teskari tartibda saralash


class Claps(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='claps_users')
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True, related_name='claps')
    count = models.IntegerField()

    def __str__(self):
        return str(self.count)

    class Meta:
        db_table = "clap"  # Jadval nomi
        verbose_name = "Clap"  # Modelning inson o'qiy oladigan nomi
        verbose_name_plural = "Claps"  # Ko‘plik shakli
        ordering = ["-count"]  # Claplar soni bo'yicha tartiblanadi
