# create_posts.py


def main():
    fake = Faker()

    for i in range(30):
        post = Post.objects.create(
            title=fake.sentence()[:28],
            content=fake.paragraph(nb_sentences=5),
            author=random.choice(User.objects.all())
            # author=User.objects.first(),  # You may need to adjust this based on your User model
        )
        print(f"Created post. Title: {post.title}  Author: {post.author.nickname}")

    post_count = Post.objects.count()

    print(f"There are {post_count} posts in the database")


if __name__ == "__main__":
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cvlab_project.settings")
    application = get_wsgi_application()

    import random
    from faker import Faker

    from post.models import Post
    from user.models import User

    # main()
