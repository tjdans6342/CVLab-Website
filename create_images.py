# create_images.py


def main():
    fake = Faker()

    users = User.objects.all()
    content_type_gallery = ContentType.objects.get(model="gallery")

    for i in range(20):
        user = random.choice(users)
        object_id = random.randint(5, 35)

        # 존재하는 인스턴스인 경우, 유니크에 걸리므로 재설정
        while Image.objects.filter(
            user=user, content_type=content_type_gallery, object_id=object_id
        ):
            user = random.choice(users)
            object_id = random.randint(5, 35)

        image = Image.objects.create(
            user=user,
            content_type=content_type_gallery,
            object_id=object_id,
            image=f"gallery/gallery_image{i+1}.jpg",  # Assign the image file path here
        )

        # fmt: off
        print(f"Created image. User: {image.user}, Content Type: {image.content_type}, Image Path: {image.image.url}")
        # fmt: on

    image_count = Image.objects.count()
    print(f"There are {image_count} images in the database")


if __name__ == "__main__":
    import os

    from django.core.wsgi import get_wsgi_application

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cvlab_project.settings")
    application = get_wsgi_application()

    import random
    from faker import Faker
    from django.contrib.contenttypes.models import ContentType

    from main.models import Image
    from user.models import User

    # main()
