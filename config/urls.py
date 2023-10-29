from django.contrib import admin
from django.urls import include, path

from accounts.views import login_view, logout_view, register_view

from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("admin/", admin.site.urls),
    path("articles/", include("articles.urls")),
    path("recipes/", include("recipes.urls")),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
]
