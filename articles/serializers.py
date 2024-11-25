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
        fields = ['user', 'count']

# Articles Serializer
class ArticlesSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    topics = TopicsSerializer(read_only=True, many=True)
    print(topics, 's')
    claps = serializers.SerializerMethodField()

    class Meta:
        model = Articles
        fields = [
            'id', 'author', 'title', 'summary', 'content', 'status',
            'thumbnail', 'topics', 'created_at', 'updated_at', 'claps', 'views_count', 'reads_count'
        ]

    def get_claps(self, obj):
        claps = obj.claps.all()
        return ClapsSerializer(claps, many=True).data