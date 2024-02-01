# count_models.py


def main():
    print(f"There are {User.objects.all().count()} users in the database")
    print(f"There are {Post.objects.all().count()} posts in the database")
    print(f"There are {Gallery.objects.all().count()} galleries in the database")
    print(f"There are {News.objects.all().count()} news in the database")

    print(f"There are {Comment.objects.all().count()} comments in the database")
    print(f"There are {Image.objects.all().count()} images in the database")
    print(f"There are {Like.objects.all().count()} likes in the database")
    print(f"There are {Dislike.objects.all().count()} dislikes in the database")


if __name__ == "__main__":
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cvlab_project.settings")
    application = get_wsgi_application()

    from user.models import User
    from post.models import Post
    from gallery.models import Gallery
    from news.models import News
    from main.models import Comment, Image, Like, Dislike

    main()
