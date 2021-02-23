from django.db import models


class Genre(models.Model):
    """Модель жанра, к которому относится произведение."""
    name = models.CharField('жанр', max_length=200, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name
