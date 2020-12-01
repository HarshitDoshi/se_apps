from django.urls import path

from .views import (
    index_view,
    create_client_view,
    dashboard_view,
    sign_in_view,
    sign_out_view,
)

app_name = "shree_finance"
urlpatterns = [
    path("home/", index_view, name="home"),
    path("create/", create_client_view, name="create_client"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("signin/", sign_in_view, name="sign_in"),
    path("signout/", sign_out_view, name="sign_out"),
]