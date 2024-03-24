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
    fields = '__all__'

class LatexView(ListView):
    model = Post
    template_name = 'latex_test.html'

