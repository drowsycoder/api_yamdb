from api.models import EmailAuth
from rest_framework.generics import CreateAPIView


class EmailAuthView(CreateAPIView):
    queryset = EmailAuth.objects.all()
    # serializer_class = EmailAuthSerializer
