from django.db import models
from django.contrib.auth.models import User

from markdownx.models import MarkdownxField


class Post(models.Model):
    title = models.CharField(max_length=255)

    post_tag = models.CharField(max_length=255, default="no tag")

    # CASCADE will delete all posts for users that no longer exist
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self) -> str:
        return self.title + ' | ' + str(self.author)
    


class MyModel(models.Model):
    myfield = MarkdownxField()
