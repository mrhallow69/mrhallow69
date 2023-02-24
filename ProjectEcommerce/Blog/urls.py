from django.urls import path

from Blog import views

urlpatterns = [
    path("",views.index,name="Bloghome")
]