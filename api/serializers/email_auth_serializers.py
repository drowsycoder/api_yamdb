from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ..models import EmailAuth

User = get_user_model()


class EmailAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailAuth
        fields = ('email',)


class EmailCodePairSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].required = False
        # email = kwargs['data']['email']
        # username = email.split('@')[0]
        # self.user, created = User.objects.get_or_create(email=email, username=username)

    def validate(self, attrs):
        email = attrs.get('email')
        username = email.split('@')[0]
        self.user, created = User.objects.get_or_create(
            email=attrs.get('email'), username=username
        )
        attrs.update({'password': ''})
        data = {}  # super().validate(attrs)
        refresh = self.get_token(self.user)
        data['token'] = str(refresh.access_token)
        return data
