from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()

class Topics(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'

class Articles(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topics = models.ManyToManyField(Topics)
    title = models.CharField(max_length=255)
    summary = models.TextField()
    content = models.TextField()
    status = models.CharField(max_length=50)
    thumbnail = models.ImageField(upload_to='articles/thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} : {self.status}'