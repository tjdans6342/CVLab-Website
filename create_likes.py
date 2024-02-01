# create_likes.py


def main():
    users = User.objects.all()
    content_types = ContentType.objects.filter(
        model__in=["post", "gallery", "news", "comment"]
    )

    for i in range(400):
        user = random.choice(users)
        content_type = random.choice(content_types)
        object_id = random.randint(5, 35)

        # 존재하는 인스턴스인 경우, 유니크에 걸리므로 재설정
        while Like.objects.filter(
            user=user, content_type=content_type, object_id=object_id
        ):
            user = random.choice(users)
            content_type = random.choice(content_types)
            object_id = random.randint(5, 35)

        like = Like.objects.create(
            user=user,
            content_type=content_type,
            object_id=object_id,
        )

        # fmt: off
        print(f"Created like. User: {like.user}, Content Type: {like.content_type} | {i+1}th like")
        # fmt: on

    like_count = Like.objects.count()
    print(f"There are {like_count} likes in the database")


if __name__ == "__main__":
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cvlab_project.settings")
    application = get_wsgi_application()

    import random
    from django.contrib.contenttypes.models import ContentType

    from main.models import Like
    from user.models import User

    # main()
