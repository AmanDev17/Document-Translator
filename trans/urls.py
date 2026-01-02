# trans/urls.py
from django.urls import path
from .views import index, translate_file

urlpatterns = [
    path("", index, name="index"),
    path("translate/", translate_file, name="translate_file"),
]
