from django.urls import path

from Student import views

urlpatterns = [
    path('', views.log, name='login'),
    path('log', views.logdata, name='logdata'),
    path('reg', views.reg, name='reg'),
    path('regdata', views.regdata, name='regdata'),
    path('home', views.home, name='home'),
    path('add', views.add, name='add'),
    path('main', views.main, name='main'),
    path('display', views.display, name='display'),
    path('update/<int:id>', views.update, name='update'),
    path('dlt/<int:id>', views.delete, name='dlt')
]
