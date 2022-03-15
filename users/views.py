# from django.shortcuts import render
# from django.shortcuts import render, redirect, HttpResponseRedirect,get_object_or_404
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
# from django.contrib.auth.models import Group
# from django.views.generic import View 
# from django.contrib import messages
# # Create your views here.

# from users import models
# from users.forms import *
# # import from warehouse.
# from warehouse.decorators import *
# from warehouse import views, models

from rest_framework import viewsets
from rest_framework import permissions
from users.serializers import UserSerializer
from users.models import CustomUser


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = CustomUser.objects.all().order_by('-date_of_birth')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

#Customer Registration

# def customerSignup(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         phone_number= request.POST['phone_number']
#         address= request.POST['address']
#         password = request.POST['password']
#         password2 = request.POST['password2']
#         if password == password2:
#             if User.objects.filter(email=email).exists():
#                 messages.info(request,'Email already exits')
#                 return redirect('customerSignup')
#             elif User.objects.filter(username=username).exists():
#                 messages.info(request,'User already exists')
#                 return redirect('customerSignup')
#             else:
#                 user = User.objects.create_user(username=username,email=email,password=password)
#                 user.save()
#                 if Group.objects.filter(name='customer').exists():
#                     group = Group.objects.get(name='customer') 
#                 else:
#                     group = Group(name="customer")
#                     group.save()
#                 user.groups.add(group)
#                 customer= Customer.objects.create(user=user,email=email,phone_number=phone_number,address=address)
#                 customer.user=user
#                 customer.save()
#                 messages.success(request,'New Customer successfully Registered')
#                 return redirect('customerlogin')
#         else: 
#             messages.info(request, "Password didn't matched")
#         return redirect('customerSignup')
#     else:
#         return render(request,'users/customerReg.html')

# #Customer Login

# @login_excluded('index')
# def customerlogin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password= password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'Customer login successful')
#             return redirect('customerpage')
#         else: 
#             messages.error(request, ' Invalid Credentials')
#             return redirect('customerlogin')
#     else:
#         return render(request,'users/customerlogin.html')
        
# #Suppliers Registration

# def supplierSignup(request):
#         if request.method == 'POST':
#             email = request.POST['email']
#             phone_number= request.POST['phone_number']
#             address= request.POST['address']
#             form = UserForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 user = User.objects.get(username=form.cleaned_data.get('username'), email=form.cleaned_data.get('email'))
#                 if Group.objects.filter(name='supplier').exists():
#                     group = Group.objects.get(name='supplier')
#                 else:
#                     group = Group(name="supplier")
#                     group.save()
#                 user.groups.add(group)
#                 supplier= Supplier.objects.create(user=user, email=email, phone_number=phone_number, address=address)
#                 supplier.user=user
#                 supplier.save()
#                 messages.success(request,'New Supplier successfully Registered')
#                 return redirect('supplierlogin')
#             else:
#                 context = { 'form' : form }
#                 return render(request, 'supplierReg.html', context=context)
#         else:
#             context = { 'form' : UserForm }
#             return render(request, 'users/supplierReg.html', context=context)

# # Customer Dashboard Page

# @login_excluded('index')
# def supplierlogin(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(username=username, password= password)
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'Supplier login successful')
#             return redirect('supplierpage')
#         else: 
#             messages.error(request, ' Invalid Credentials')
#             return redirect('supplierlogin')
#     else:
#         return render(request,'users/supplierlogin.html')

# # Customer Dashboard Page

# @login_required(login_url='customerlogin')
# @allowed_users(allowed_groups=['customer'])
# def customerpage(request):
#     customer=Customer.objects.get(user_id=request.user.id)
#     orders= Order.objects.filter(customer_id = customer)
#     context={
#         'orders':orders,
#         'customer':customer,
#     }
#     return render(request,'users/customerpage.html',context)

# #Supplier Dashboard Page

# @login_required(login_url='supplierlogin')
# @allowed_users(allowed_groups=['supplier'])
# def supplierpage(request):
#     supplier=Supplier.objects.get(user_id=request.user.id)
#     product= Product.objects.filter(supplier_id=supplier)
#     product_count= product.count()
    
#     context={
#         'supplier':supplier,
#         'product':product,
#         'product_count':product_count,
#     }
#     return render(request,'users/supplierpage.html',context)

# #Logout

# def userlogout(request):
#     logout(request)
#     return redirect('index')
