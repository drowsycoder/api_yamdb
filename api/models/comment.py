from django.db import models

from .user import User
from .review import Review


class Comment(models.Model):
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE,
                                 related_name='comments')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comments')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
