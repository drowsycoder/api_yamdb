from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .models import Category, Comment, Genre, Review, Title, User
from .models import User

admin.site.register(User, UserAdmin)
