from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from user.models import User


class Comment(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True)

    comment = models.TextField(max_length=150, blank=False)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    related_object = GenericForeignKey()

    likes = GenericRelation("Like", related_query_name="comment")
    dislikes = GenericRelation("DisLike", related_query_name="comment")

    def __str__(self):
        return f"({self.user}, {self.related_object})"

    class Meta:
        unique_together = ["user", "content_type", "object_id"]


class Image(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True)

    image = models.ImageField(upload_to="pics")

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="images")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    related_object = GenericForeignKey()

    def __str__(self):
        return f"({self.user}, {self.related_object})"

    class Meta:
        unique_together = ["user", "content_type", "object_id"]


class Like(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    related_object = GenericForeignKey()

    def __str__(self):
        return f"({self.user}, {self.related_object})"

    class Meta:
        unique_together = ["user", "content_type", "object_id"]


class Dislike(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="dislikes")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()

    related_object = GenericForeignKey()

    def __str__(self):
        return f"({self.user}, {self.related_object})"

    class Meta:
        unique_together = ["user", "content_type", "object_id"]
