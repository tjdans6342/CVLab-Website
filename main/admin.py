from django.contrib import admin
from .models import Comment, Image, Like, Dislike

# Image
admin.site.register(Image)

# Comment
admin.site.register(Comment)

# Like
admin.site.register(Like)

# Dislike
admin.site.register(Dislike)
