from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Post, MyModel

# Register your models here.

# This will make the blog post entries to be accessible from admin area
admin.site.register(Post)
admin.site.register(MyModel, MarkdownxModelAdmin)
