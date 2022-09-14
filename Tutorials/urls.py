from django.urls import path
from Tutorials import views
urlpatterns = [
    # in tutorialss table links , url and name must be same so page can be accessed

    path('c/', views.c_tutorial, name='c'),
    path('java/', views.java_tutorial, name='java'),
    path('html/', views.html_tutorial, name='html'),
    path('css/', views.css_tutorial, name='css'),
    path('python/', views.python_tutorial, name='python'),
    path('android/', views.android_tutorial, name='android'),
    path('django/', views.django_tutorial, name='django'),

]