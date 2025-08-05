from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView   
from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
    