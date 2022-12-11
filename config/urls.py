from django.contrib import admin
from django.urls import path

from . import views
from articles import views as article_views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("admin/", admin.site.urls),
    path('articles/', article_views.article_search_view,  name="article-search"),
    path('articles/create', article_views.article_create_view,  name="article-create"),
    path('articles/<int:id>/', article_views.article_detail_view, name="article-detail"),
]
