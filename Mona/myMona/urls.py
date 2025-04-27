from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Login", views.Login, name="Login"),
    path("Signup", views.Signup, name="Signup"),
    path("Logout", views.Logout, name="Logout"),
    path("generate-blog", views.generate_blog, name="generate-blog")
]
