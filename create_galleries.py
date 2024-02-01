# create_galleries.py


def main():
    fake = Faker()

    for i in range(10):
        gallery = Gallery.objects.create(
            title=f"gallery_example ({i+1})",
            author=random.choice(User.objects.all()),
        )
        # fmt: off
        print(f"Created gallery. Title: {gallery.title}  Author: {gallery.author.nickname}")
        # fmt:on

    gallery_count = Gallery.objects.count()

    print(f"There are {gallery_count} galleries in the database")


if __name__ == "__main__":
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cvlab_project.settings")
    application = get_wsgi_application()

    import random
    from faker import Faker

    from gallery.models import Gallery
    from user.models import User

    # main()
