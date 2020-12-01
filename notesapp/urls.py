from django.urls import path

from .views import (
    index_view,
    sign_in_view,
    sign_out_view,
)

app_name = "notesapp"
urlpatterns = [
    path("home/", index_view, name="home"),
]