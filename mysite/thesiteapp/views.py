from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = 'index.html'


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm # takes care of what fields to display (see forms.py)
    template_name = 'add_post.html'
    # fields = '__all__'
    # fields = ('title', 'post_tag', 'author', 'body') # this is from models.py. possible to display only a few with a tuples
    
