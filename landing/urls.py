from django.urls import path
from .views import home, subscribe, open_post

urlpatterns = [
    path('', home, name='landing_page'),
    path("subscribe/", subscribe, name="subscribe"),
    path("open_post/", open_post, name="open_post"),
]