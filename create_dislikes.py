# create_dislikes.py


def main():
    users = User.objects.all()
    content_types = ContentType.objects.filter(
        model__in=["post", "gallery", "news", "comment"]
    )

    for i in range(100):
        user = random.choice(users)
        content_type = random.choice(content_types)
        object_id = random.randint(5, 35)

        # 존재하는 인스턴스인 경우, 유니크에 걸리므로 재설정
        while Dislike.objects.filter(
            user=user, content_type=content_type, object_id=object_id
        ):
            user = random.choice(users)
            content_type = random.choice(content_types)
            object_id = random.randint(5, 35)

        dislike = Dislike.objects.create(
            user=user,
            content_type=content_type,
            object_id=object_id,
        )

        # fmt: off
        print(f"Created dislike. User: {dislike.user}, Content Type: {dislike.content_type} | {i+1}th dislike")
        # fmt: on

    dislike_count = Dislike.objects.count()
    print(f"There are {dislike_count} dislikes in the database")


if __name__ == "__main__":
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cvlab_project.settings")
    application = get_wsgi_application()

    import random
    from django.contrib.contenttypes.models import ContentType

    from main.models import Dislike
    from user.models import User

    # main()
