from django.urls import path, include
from .views import PostListView
from django.views.generic import DetailView, CreateView
from .models import Post

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', DetailView.as_view(model=Post, template_name='post_detail.html'), name='post_detail'),
    path('post/new/', CreateView.as_view(model=Post, template_name='post_new.html', fields=['title', 'content']), name='post_new'),
]