from django.urls import path
from . import views

urlpatterns = [
    path('customer/registration', views.customerSignup, name='customerSignup'),
    path('customer/login', views.customerlogin, name='customerlogin'),
    path('supplier/registration', views.supplierSignup, name='supplierSignup'),
    path('supplier/login', views.supplierlogin, name='supplierlogin'),
    path('customerpage', views.customerpage, name='customerpage'),
    path('supplierpage', views.supplierpage, name='supplierpage'),
    path('userlogout', views.userlogout, name='userlogout'),
    ]