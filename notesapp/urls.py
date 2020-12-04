from django.urls import path

from .views import (
    index_view,
    dashboard_view,
    create_note_view,
    sign_in_view,
    sign_out_view,
)

app_name = "notesapp"
urlpatterns = [
    path("home/", index_view, name="home"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("create/", create_note_view, name="create"),
]