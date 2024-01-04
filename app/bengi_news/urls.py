from django.urls import path
from . import views

page_routes = [
    path("", views.index, name="index"),
]

htmx_routes = [
    path('fetch-news/', views.fetch_news, name='fetch-news'),
]

urlpatterns = page_routes + htmx_routes
