from rest_framework import serializers
from .models import Article, Topic, Clap
from django.contrib.auth import get_user_model
User = get_user_model()


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'email', 'avatar']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name', 'description', 'is_active']


class ClapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clap
        fields = ['user', 'count']

# Articles Serializer

class ArticleCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Article
        fields = ['title', 'content', 'author']

    def create(self, validated_data):
        user = self.context['request'].user
        article = Article.objects.create(author=user, **validated_data)
        return article

class ArticleDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    topics = TopicSerializer(read_only=True, many=True)
    claps = ClapSerializer(read_only=True, many=True)

    class Meta:
        model = Article
        fields = [
            'id', 'author', 'title', 'summary', 'content', 'status',
            'thumbnail', 'topics', 'views_count', 'reads_count', 'created_at', 'updated_at', 'claps'
        ]