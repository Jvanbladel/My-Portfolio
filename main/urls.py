from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("work/", views.work, name="work"),
    path("resume/", views.resume, name="resume"),
    path("contact/", views.contact, name="contact"),
]
