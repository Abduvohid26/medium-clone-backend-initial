from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Article(models.Model):
    author = models.ForeignKey(User, related_name='articles', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='articles/thumbnails/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('publish', 'Publish')], default='pending')
    topics = models.ManyToManyField('Topic', related_name='articles')
    views_count = models.IntegerField(default=0)
    reads_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Clap(models.Model):
    user = models.ForeignKey(User, related_name='claps', on_delete=models.CASCADE)
    article = models.ForeignKey('Article', related_name='claps', on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} clapped for {self.article.title}"


