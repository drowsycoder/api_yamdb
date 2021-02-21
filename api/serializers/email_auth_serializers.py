from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ..models import EmailAuth

User = get_user_model()


class EmailAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailAuth
        fields = ('email',)


class EmailCodePairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField()
    confirmation_code = serializers.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False

    def check_conf_code(self, email, confirmation_code):
        try:
            email_code = EmailAuth.objects.get(
                email=email, confirmation_code=confirmation_code)
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                'Didn\'t find such email and confirmation code combination. '
                'Please get email notification with confirmation code and '
                'post email and code to get token')
        email_code.delete()
        return True

    def validate(self, attrs):
        email = attrs['email']
        confirmation_code = attrs['confirmation_code']
        if self.check_conf_code(email, confirmation_code):
            username = email.split('@')[0]
            self.user, _ = User.objects.get_or_create(
                email=attrs.get('email'), username=username
            )
            token = self.get_token(self.user)
            data = {'token': str(token.access_token)}
            return data
        raise serializers.ValidationError(
            'Something gone wrong')
