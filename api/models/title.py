from django.db import models

from .category import Category
from .genre import Genre


class Title(models.Model):
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 related_name='categories')
    genre = models.ManyToManyField(Genre, related_name='genres')
    name = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
