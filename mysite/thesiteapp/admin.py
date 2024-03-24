from django.contrib import admin
from .models import Post

# Register your models here.

# This will make the blog post entries to be accessible from admin area
admin.site.register(Post)
