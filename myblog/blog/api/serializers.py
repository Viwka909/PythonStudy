from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Category, Post, Comment

class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для пользователей"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        read_only_fields = ['id']

class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий"""
    post_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'post_count']
        read_only_fields = ['id']
    
    def get_post_count(self, obj):
        return obj.post_set.filter(is_published=True).count()

class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев"""
    author_name = serializers.CharField(source='author.username', read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'author_name', 'created_at', 'post']
        read_only_fields = ['id', 'author', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для постов"""
    author_name = serializers.CharField(source='author.username', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'content', 'author', 'author_name',
            'category', 'category_name', 'created_at', 'updated_at',
            'is_published', 'comments', 'comment_count'
        ]
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']
    
    def get_comment_count(self, obj):
        return obj.comments.count()

class PostCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания постов (без связанных данных)"""
    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'is_published']
    
    def create(self, validated_data):
        # Автоматически устанавливаем автором текущего пользователя
        validated_data['author'] = self.context['request'].user
        return super().create(validated_data)