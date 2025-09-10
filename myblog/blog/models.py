# blog/models.py
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    """Модель категории для постов"""
    name = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='URL')
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self):
        return self.name

class Post(models.Model):
    """Модель поста блога"""
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='URL')
    content = models.TextField(verbose_name='Содержание')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    is_published = models.BooleanField(default=False, verbose_name='Опубликован')
    
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    """Модель комментария"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст комментария')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f'Комментарий от {self.author} к посту {self.post}'


