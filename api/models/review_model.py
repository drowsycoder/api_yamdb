from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .title_model import Title
from .user_model import User


class Review(models.Model):
    title = models.ForeignKey(Title, on_delete=models.CASCADE,
                              related_name='reviews',
                              verbose_name='произведение')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='reviews',
                               verbose_name='автор')
    score = models.PositiveSmallIntegerField('оценка',
                                             validators=[MinValueValidator(1),
                                                         MaxValueValidator(10)]
                                             )
    pub_date = models.DateTimeField('дата публикации', auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['author', 'title'],
                                               name='unique_review')]
