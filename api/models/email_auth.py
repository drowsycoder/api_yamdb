from smtplib import SMTPException

from django.core.mail import send_mail
from django.db import models
from django.utils.crypto import get_random_string

SUBJECT = 'YaMDb API registration letter'


class EmailAuth(models.Model):
    email = models.EmailField('адрес электронной почты', unique=True)
    confirmation_code = models.CharField(max_length=32)

    def save(self, *args, **kwargs):
        self.confirmation_code = get_random_string(32)
        message = f'confirmation_code: {self.confirmation_code}'
        try:
            send_mail(
                SUBJECT, message, from_email=None, recipient_list=[self.email]
            )
        except SMTPException:
            return None

        super().save(*args, **kwargs)
