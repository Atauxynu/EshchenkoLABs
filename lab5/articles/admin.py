from django.contrib import admin
from .models import Article


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    """Данный класс нужен для описания того, как модель Article отображается в админской панели"""
    list_display = ('title', 'author', 'get_excerpt', 'created_date')


# Данная функция объявляет, что модель должна быть добавлена в интерфейс администратора
admin.site.register(Article, ArticleAdmin)
