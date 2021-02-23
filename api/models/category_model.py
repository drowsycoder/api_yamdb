from django.db import models


class Category(models.Model):
    """Модель категории, к которой относится произведение."""
    name = models.CharField('категория', max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
