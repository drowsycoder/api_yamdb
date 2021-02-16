from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(verbose_name='Биография')
    role = models.CharField(verbose_name='Роль в API')


# first_name
# last_name
# username
# bio
# email
# role
