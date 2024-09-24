from rest_framework.viewsets import ModelViewSet
from .serializers import AuthorSerializer, TopicsSerializer, ArticlesSerializer
from .models import Topics, Articles
from rest_framework import permissions
from rest_framework.response import Response
from django.contrib.auth import get_user_model
User = get_user_model()

class ArticleViewSet(ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer
    permission_classes = [permissions.IsAuthenticated]