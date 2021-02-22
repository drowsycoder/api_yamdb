from smtplib import SMTPException

from django.core.mail import send_mail
from django.db import models
from django.utils.crypto import get_random_string

SUBJECT = 'YaMDb API registration letter'
RANDOM_STRING_LENGTH = 32


class EmailAuth(models.Model):
    """
    Stores email, confirmation code and datetime added.
    Sends message with confirmation code to that email.
    Email and confirmation code are used to generate JWT token.
    """

    email = models.EmailField('адрес электронной почты', unique=True)
    confirmation_code = models.CharField(max_length=RANDOM_STRING_LENGTH)
    added = models.DateTimeField(
        verbose_name='дата запроса', auto_now_add=True
    )

    def save(self, *args, **kwargs):
        self.confirmation_code = get_random_string(RANDOM_STRING_LENGTH)
        message = f'confirmation_code: {self.confirmation_code}'
        try:
            send_mail(
                SUBJECT, message, from_email=None, recipient_list=[self.email]
            )
        except SMTPException:
            return None

        super().save(*args, **kwargs)
