from django.urls import path

from Shop import views

urlpatterns = [
    path("", views.index, name="shophome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("tracker/", views.tracker, name="Track"),
    path("search/", views.search, name="Search"),
    path("productview/", views.prodview, name="ProdView"),
    path("checkout/", views.checkout, name="Checkout"),
]
