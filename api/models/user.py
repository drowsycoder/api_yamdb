from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    USER = 'U'
    ADMIN = 'A'
    MODERATOR = 'M'

    ROLE_CHOICES = [(USER, 'user'), (ADMIN, 'admin'), (MODERATOR, 'moderator')]

    bio = models.TextField('о себе', blank=True, null=True)
    role = models.CharField(
        'роль в API', max_length=1, choices=ROLE_CHOICES, default=USER
    )
    email = models.EmailField('адрес электронной почты', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
