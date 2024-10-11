from rest_framework import serializers
from .models import Articles, Topics, Claps
from django.contrib.auth import get_user_model
User = get_user_model()

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'middle_name', 'email', 'avatar']

class TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = ['id', 'name', 'description', 'is_active']

class ClapsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claps
        fields = ['name']

class ArticlesSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    topics = TopicsSerializer(many=True, read_only=True)
    claps = serializers.SerializerMethodField()

    class Meta:
        model = Articles
        fields = [
            'id', 'author', 'title', 'summary', 'content', 'status',
            'thumbnail', 'topics', 'created_at', 'updated_at', 'claps'
        ]

    def get_claps(self, obj):
        return obj.claps if obj.claps is not None else []
