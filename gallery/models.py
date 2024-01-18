from django.db import models

from user.models import User


# Create your models here.
class Gallery(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="gallreies")

    # likes = GenericRelation("Like", related_query_name="review")
    # dislikes = GenericRelation("DisLike", related_query_name="review")
    # images
    # comments

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-dt_created"]