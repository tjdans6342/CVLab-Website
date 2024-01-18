from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from main.models import Comment, Dislike, Image, Like
from user.models import User


# Create your models here.
class Post(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")

    likes = GenericRelation(Like, related_query_name="post")
    dislikes = GenericRelation(Dislike, related_query_name="post")
    images = GenericRelation(Image, related_query_name="post")
    comments = GenericRelation(Comment, related_query_name="post")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-dt_created"]
