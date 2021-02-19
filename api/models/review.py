from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .title import Title
from .user import User


class Review(models.Model):
    title_id = models.ForeignKey(Title, on_delete=models.CASCADE,
                                 related_name='reviews',
                                 verbose_name='произведение')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='reviews',
                               verbose_name='автор')
    score = models.PositiveSmallIntegerField('оценка',
        validators=[MinValueValidator(1),MaxValueValidator(10)])
    pub_date = models.DateTimeField('дата публикации', auto_now_add=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['title_id', 'author'],
                                               name='unique_review')]
