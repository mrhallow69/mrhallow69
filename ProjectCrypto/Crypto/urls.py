from django.urls import path

from Crypto import views

urlpatterns = [
    path("", views.home, name="home"),
    path("prices", views.prices, name="prices")
]
