from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.views import TokenObtainPairView

from api.models import EmailAuth
from api.serializers import EmailAuthSerializer, EmailCodePairSerializer

User = get_user_model()


class EmailAuthView(CreateAPIView):
    queryset = EmailAuth.objects.all()
    serializer_class = EmailAuthSerializer


class EmailCodeView(TokenObtainPairView):
    serializer_class = EmailCodePairSerializer
