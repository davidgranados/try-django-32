from django.contrib import admin

from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "slug",
        "content",
        "timestamp",
        "updated",
    ]
    list_display_links = ["title", "content"]
    search_fields = ["title", "content"]
