from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model for api yamdb.
    Email used as username field.
    New fields: bio, role.
    """

    class Role(models.TextChoices):
        USER = 'user', ('user')
        MODERATOR = 'moderator', ('moderator')
        ADMIN = 'admin', ('admin')

    bio = models.TextField('о себе', blank=True, null=True)
    role = models.CharField(
        'роль в API', max_length=9, choices=Role.choices, default=Role.USER
    )
    email = models.EmailField('адрес электронной почты', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
