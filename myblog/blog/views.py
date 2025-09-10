
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, Category

class PostListView(ListView):
    """Список всех опубликованных постов"""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        return Post.objects.filter(is_published=True)

class PostDetailView(DetailView):
    """Детальная страница поста"""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        return Post.objects.filter(is_published=True)

class CategoryPostListView(ListView):
    """Посты определенной категории"""
    template_name = 'blog/category_posts.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Post.objects.filter(category=category, is_published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context

def about(request):
    """Страница 'О нас'"""
    return render(request, 'blog/about.html')
