from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('about/', views.about, name='about'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('category/<slug:slug>/', views.CategoryPostListView.as_view(), name='category_posts'),
]