from .models import Article, Topic, Claps
from django.contrib import admin


admin.site.register([Article, Topic, Claps])