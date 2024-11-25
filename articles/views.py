from rest_framework import viewsets
from .models import Article
from .serializers import ArticleCreateSerializer, ArticleDetailSerializer

class ArticlesView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return ArticleCreateSerializer
        return ArticleDetailSerializer