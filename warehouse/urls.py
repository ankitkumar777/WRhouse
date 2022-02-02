from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('stockrequests', views.stockreq, name='stockrequests'),
    path('products', views.products, name='products'),
    # path('products',views.ProductView.as_view(), name='products'),
    path('createproduct/<str:id>/', views.createproduct, name='createproduct'),
    path('createorder/<str:id>/', views.CreateOrderView.as_view(), name='createorder'),
    path('updateorder/<str:pk>/', views.updateorder, name='updateorder'),
    path('deleteorder/<str:pk>/', views.deleteorder, name='deleteorder'),
    path('orderdelivery/', views.orderdelivery, name='orderdelivery'),

]

 