from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("luka", views.luka, name="luka"),
    path("marusia", views.marusia, name="marusia")
]