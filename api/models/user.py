from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField('о себе')
    role = models.CharField('роль в API', max_length=31)
    email = models.EmailField('адрес электронной почты', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
