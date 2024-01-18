from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from main.models import Dislike, Like
from user.models import User


# Create your models here.
class News(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)

    content = models.TextField(blank=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news")

    likes = GenericRelation(Like, related_query_name="news")
    dislikes = GenericRelation(Dislike, related_query_name="news")

    def __str__(self):
        return self.title[:30]

    class Meta:
        ordering = ["-dt_created"]
