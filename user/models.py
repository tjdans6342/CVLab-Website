from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(
        max_length=15,
        unique=True,
        null=True,
        # validators=[validate_no_special_characters],
        error_messages={"unique": "이미 사용중인 닉네임입니다."},
    )

    profile_pic = models.ImageField(
        default="default_profile_pic.jpg",
        upload_to="profile_pics",
        blank=True,
    )

    intro = models.CharField(max_length=60, blank=True)

    RANK_CHOICES = [
        (1, "user"),
        (2, "manager"),
        (3, "admin"),
    ]
    rank = models.IntegerField(choices=RANK_CHOICES, default=1)

    def __str__(self):
        return self.email
