from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from .models import Comment, Review
from .models import Category, Genre, Title, User


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'slug', 'name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'slug', 'name',)
    search_fields = ('name',)
    empty_value_display = '-пусто-'


class TitleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'year', 'genre', 'category', 'description',)
    search_fields = ('name', 'description',)
    list_filter = ('year', 'genre', 'category',)
    empty_value_display = '-пусто-'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(User, UserAdmin)
