from django.urls import path
from . import views

page_routes = [
    path("", views.index, name="index"),
]

htmx_routes = []

urlpatterns = page_routes + htmx_routes
