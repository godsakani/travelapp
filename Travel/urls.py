from django.contrib import admin
from django.urls import path
from .views import adminorders,acceptorder,declineorder, homepageview, deletebus, addbus, adminloginview,adminhomepageview,authenticateadmin,logoutadmin, placeorder, signupuser, userauthenticate, userloginview, customerwelcomeview, userlogout, userorders
urlpatterns = [
    path('admin/',adminloginview,name='adminloginpage'),
    path('adminauthenticate/',authenticateadmin),
    path('admin/homepage/',adminhomepageview,name = 'adminhomepage'),
    path('adminlogout/',logoutadmin),
    path('addbus/',addbus),
    path('deletebus/<int:busapk>/',deletebus),
    path('',homepageview, name = 'homepage'),
    path('signupuser/',signupuser),
    path('loginuser/',userloginview, name = 'userloginpage'),
    path('customer/welcome/',customerwelcomeview, name = 'customerpage'),
    path('customer/authenticate/',userauthenticate),
    path('userlogout/',userlogout),
    path('placeorder/',placeorder),
    path('userorders/',userorders),
    path('adminorders/',adminorders),
    path('acceptorder/<int:orderpk>/',acceptorder),
    path('declineorder/<int:orderpk>/',declineorder),
]
 