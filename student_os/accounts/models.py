from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    college_email = models.EmailField(unique=True)
    roll_number = models.CharField(max_length=20)
    batch = models.CharField(max_length=20)

    ROLE_CHOICES = [
        ("student", "Student"),
        ("faculty", "Faculty"),
        ("admin", "Admin"),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="student"
    )

    def __str__(self):
        return self.username
