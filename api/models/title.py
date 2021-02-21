from django.db import models

from . import Category, Genre


class Title(models.Model):
    name = models.CharField('название', max_length=100)
    year = models.PositiveSmallIntegerField('год', blank=True, null=True)
    # rating = models.PositiveSmallIntegerField()
    description = models.TextField('описание', blank=True, null=True)
    genre = models.ManyToManyField(
        Genre,
        related_name='titles',
        verbose_name='связанный жанр',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        verbose_name='связанная категория',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
