from django.urls import path
from users import views

urlpatterns = [
    path('all/', views.UserViewSet.as_view({'get': 'list'}), name='user'),
    # path('customer/login', views.customerlogin, name='customerlogin'),
    # path('supplier/registration', views.supplierSignup, name='supplierSignup'),
    # path('supplier/login', views.supplierlogin, name='supplierlogin'),
    # path('customerpage', views.customerpage, name='customerpage'),
    # path('supplierpage', views.supplierpage, name='supplierpage'),
    # path('userlogout', views.userlogout, name='userlogout'),
    ]