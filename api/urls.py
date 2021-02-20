from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet, EmailAuthView, EmailCodeView,
                    GenreViewSet, TitleViewSet, UserViewSet)

app_name = 'api'

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'titles', TitleViewSet, basename='titles')
router.register(r'users', UserViewSet, basename='users')

urlpatterns = [
    path('v1/auth/token/', EmailCodeView.as_view(), name='token_obtain_pair'),
    path('v1/auth/email/', EmailAuthView.as_view(), name="email_auth"),
    path('v1/', include(router.urls)),
]

