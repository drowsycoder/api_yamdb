from django.db import models

from .category import Category
from .genre import Genre


class Title(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(null=True, blank=True)
    # rating = models.PositiveSmallIntegerField()
    description = models.TextField(null=True, blank=True)
    genre = models.ManyToManyField(Genre, related_name='genres')
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 related_name='categories')

    def __str__(self):
        return self.name
