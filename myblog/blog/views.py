
# blog/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Category, Comment
from .forms import CommentForm

class PostListView(ListView):
    """Список всех опубликованных постов"""
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 5
    
    def get_queryset(self):
        return Post.objects.filter(is_published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем категории для боковой панели
        context['categories'] = Category.objects.all()
        return context

class PostDetailView(DetailView):
    """Детальная страница поста"""
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    
    def get_queryset(self):
        return Post.objects.filter(is_published=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем форму комментария
        context['comment_form'] = CommentForm()
        return context

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
        context['categories'] = Category.objects.all()
        return context

def about(request):
    """Страница 'О нас'"""
    return render(request, 'blog/about.html')

@login_required
def add_comment(request, slug):
    """
    Добавление комментария к посту
    Требует аутентификации пользователя
    """
    post = get_object_or_404(Post, slug=slug, is_published=True)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            
            messages.success(request, 'Ваш комментарий успешно добавлен!')
            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()
    
    return render(request, 'blog/add_comment.html', {'form': form, 'post': post})

@login_required
def delete_comment(request, comment_id):
    """
    Удаление комментария
    Только автор комментария или суперпользователь может удалить
    """
    comment = get_object_or_404(Comment, id=comment_id)
    
    # Проверяем права доступа
    if request.user == comment.author or request.user.is_superuser:
        post_slug = comment.post.slug
        comment.delete()
        messages.success(request, 'Комментарий удален.')
        return redirect('post_detail', slug=post_slug)
    else:
        messages.error(request, 'У вас нет прав для удаления этого комментария.')
        return redirect('post_detail', slug=comment.post.slug)