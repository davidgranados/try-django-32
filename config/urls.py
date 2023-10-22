from django.contrib import admin
from django.urls import path

from accounts.views import login_view, logout_view, register_view
from articles.views import article_search_view, article_create_view, article_detail_view

from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("admin/", admin.site.urls),
    path("articles/", article_search_view, name="article-search"),
    path("articles/create", article_create_view, name="article-create"),
    path("articles/<slug:slug>/", article_detail_view, name="article-detail"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
]
