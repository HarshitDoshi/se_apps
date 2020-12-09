from django.urls import path, include
from rest_framework import routers
from .views import (
    NoteView,
    index_view,
    dashboard_view,
    create_note_view,
    sign_in_view,
    sign_out_view,
)

router = routers.DefaultRouter()
router.register(r'notes', NoteView)

app_name = "notesapp"
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("home/", index_view, name="home"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("create/", create_note_view, name="create"),
]