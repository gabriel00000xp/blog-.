from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView
from  django.views.generic.edit import CreateView , UpdateView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'content', 'author']
#
#
class PostEditView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'content']

class PostUpdateView(UpdateView):
    model = Post
    template_name = 'updates-post.html'
    fields = ['title', 'content']

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')