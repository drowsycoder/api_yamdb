from django.db import models

from .review import Review
from .user import User


class Comment(models.Model):
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE,
                                  related_name='comments',
                                  verbose_name='ревью')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='comments',
                               verbose_name='автор')
    pub_date = models.DateTimeField('дата публикации', auto_now_add=True,
                                    db_index=True)
