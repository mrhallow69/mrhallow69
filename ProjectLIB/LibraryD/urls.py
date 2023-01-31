from django.urls import path

from LibraryD import views

urlpatterns = [
    path('', views.home, name='home'),
    path('studentlog', views.stulog, name='stulog'),
    path('stulogdata', views.stulogdata, name='logdata'),

    path('adminlog', views.adminlog, name='adlog'),
    path('adminlogdata', views.adminlogdata, name='adlogdata'),

    path('adminreg', views.adminreg, name='adminreg'),
    path('adregdata', views.adregdata, name='adregdata'),

    path('studreg', views.studreg, name='studreg'),
    path('studregdata', views.studregdata, name='studregdata'),

    path('adminhome', views.adminhome, name='adminhom'),
    path('studenthome', views.studenthome, name='studenthome'),

    path('add', views.add, name='addbook'),

    path('main', views.main, name='main'),

    path('display', views.display, name='display'),

    path('addbook', views.addbook, name='add'),

    path('issuebook', views.issuebook, name='issueb'),

    path('displaybook', views.displaybook, name='dbook'),

    # path('bookmain',views.mainbook,name='bmain')

]
