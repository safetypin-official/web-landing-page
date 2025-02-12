from django.urls import path
from .views import home, subscribe

urlpatterns = [
    path('', home, name='landing_page'),
    path("subscribe/", subscribe, name="subscribe"),
]