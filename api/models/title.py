from django.db import models

from .category import Category
from .genre import Genre


class Title(models.Model):
    name = models.CharField('название', max_length=100)
    year = models.PositiveSmallIntegerField('год', blank=True, null=True)
    # rating = models.PositiveSmallIntegerField()
    description = models.TextField('описание', blank=True, null=True)
    genre = models.ManyToManyField(
        Genre,
        on_delete=models.PROTECT,
        related_name='genres',
        verbose_name='связанный жанр',
        blank=True,
        null=True,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='categories',
        verbose_name='связанная категория',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
