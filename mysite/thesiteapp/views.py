from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'index.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'add_post.html'
    # fields = '__all__' <-- this imports all of them
    fields = ('title', 'post_tag') # this is from models.py. possible to display only a few with a tuples
