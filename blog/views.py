from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from  django.views.generic.edit import CreateView , UpdateView
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class PostListView( ListView):
    model = Post
    template_name = 'post_list.html'

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'content', 'author']
#
#
class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'content']

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'updates-post.html'
    fields = ['title', 'content']

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')
    
    
