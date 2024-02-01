# create_news.py


def main():
    fake = Faker()

    for i in range(30):
        news = News.objects.create(
            content=fake.paragraph(nb_sentences=3),
            author=random.choice(User.objects.all()),
        )
        # fmt: off
        print(f"Created news. content: '{news.content[:10]}...'  Author: {news.author.nickname}")
        # fmt:on

    news_count = News.objects.count()

    print(f"There are {news_count} news in the database")


if __name__ == "__main__":
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cvlab_project.settings")
    application = get_wsgi_application()

    import random
    from faker import Faker

    from news.models import News
    from user.models import User

    # main()
