# create_comments.py


def main():
    fake = Faker()

    users = User.objects.all()
    content_types = ContentType.objects.filter(model__in=["post", "gallery"])

    for i in range(200):
        user = random.choice(users)
        content_type = random.choice(content_types)
        object_id = random.randint(5, 35)

        # 존재하는 인스턴스인 경우, 유니크에 걸리므로 재설정
        while Comment.objects.filter(
            user=user, content_type=content_type, object_id=object_id
        ):
            user = random.choice(users)
            content_type = random.choice(content_types)
            object_id = random.randint(5, 35)

        comment = Comment.objects.create(
            comment=f"this is {i+1}th comments | {fake.paragraph(nb_sentences=10)[:300]}",
            user=user,
            content_type=content_type,
            object_id=object_id,
        )

        # fmt: off
        print(f"Created comment. User: {comment.user}, Content Type: {comment.content_type}, Comment: {comment.comment[:20]}...")
        # fmt: on

    comment_count = Comment.objects.count()
    print(f"There are {comment_count} Comments in the database")


if __name__ == "__main__":
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cvlab_project.settings")
    application = get_wsgi_application()

    import random
    from faker import Faker
    from django.contrib.contenttypes.models import ContentType

    from main.models import Comment
    from user.models import User

    # main()
