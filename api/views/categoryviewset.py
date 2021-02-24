from api.models import Category
from api.serializers import CategorySerializer
from api.views import CustomAPIViewSet


class CategoryViewSet(CustomAPIViewSet):
    """Представление для взаимодействия (CRUD) с категорией произведения."""
    queryset = Category.objects.all().order_by('name')
    serializer_class = CategorySerializer
