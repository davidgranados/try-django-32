from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content']
    list_display_links = ['title', 'content']
    search_fields = ['title', 'content']
