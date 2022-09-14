from django.urls import path
from EduCartApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),

# logins urls
    path('login/', views.loginUser, name='login'),
    path('loginuser', views.loginUser, name='loginuser'),
    path('logoutuser/', views.logoutuser, name='logoutuser'),
    path('signup/', views.signup, name='signup'),


#  users page access urls
    path('mycart/', views.mycart, name='mycart'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('checkout/', views.checkouts, name='checkout'),
    path('mycourses/', views.mycourses, name='mycourses'),
    path('personalinfo/', views.personalinfo, name='personalinfo'),
    path('manageaddress/', views.manageAddress, name='manageaddress'),
    path('productlist/', views.product_list, name='productlist'),
    path('product_details/', views.product_details, name='product_details'),
    path('view/', views.view, name='view'),
    path('mycart/delete/<int:id>/', views.delete, name='delete'),
    path('updateItem/', views.updateItem, name='updateItem'),
    path('process_order/', views.processOrder, name='process_order'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
