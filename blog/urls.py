from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostEditView
from django.views.generic import DetailView, CreateView
from .models import Post

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', PostEditView.as_view(), name='post_edit'),
]