from django.shortcuts import render, redirect, HttpResponseRedirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
# Create your views here.

from .decorators import allowed_users, login_excluded
from .searchfilter import ProductFilter
from warehouse.models import *
from warehouse.forms import *

# import from users
from users import views, models

# HomePage

class IndexView(View):
  def get(self, request, *args, **kwargs):
        return render(request, "index.html")


# All Warehouse Products list

def products(request):
    product = Product.objects.all().order_by('id')
    product_count = product.count()
    paginator = Paginator(product, 5, orphans=2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    searchfilter = ProductFilter(request.GET, queryset=product)
    product = searchfilter.qs 
    context = {
        'product':'product',
        'page_obj': page_obj,
        'product_count':product_count,
        'searchfilter':searchfilter,
}
    return render(request, 'warehouse/products.html', context)
    

# All Products list using class based view
# class ProductView(View):
#     model = Product
#     template_name = 'warehouse/products.html'
#     ordering = ['id']
#     paginate_by = 5
#     paginate_orphans = 1

#     def get_context_data(self, *args, **kwargs):
#         try:
#             return super(ProductListView, self).get_context_data(self, *args, **kwargs)
#         except Http404:
#             self.kwargs['page'] = 1 
#             return super(ProductListView, self).get_context_data(self, *args, **kwargs)


# Create New Customer Orders

class CreateOrderView(View):
    template_name = 'warehouse/order.html'
    
    @method_decorator(login_required(login_url='customerlogin'),
    allowed_users(allowed_groups=['customer']))
    def get(self, request, id):
        customer = Customer.objects.get(id=id)
        form = OrderForm(request.GET or None)
        product = Product.objects.all()
        context = {
            'form'      : form,
            'product'    : product
        }
        return render(request, self.template_name, context)

    @method_decorator(login_required(login_url='customerlogin'),
    allowed_users(allowed_groups=['customer']))
    def post(self, request, id):
        customer = Customer.objects.get(id=id)
        form = OrderForm(request.POST,customer)
        if form.is_valid():
            orderobj = form.save(commit=False)
            orderobj.customer=customer
            product = get_object_or_404(Product, name=orderobj.product.name)
            if  product.product_quantity < orderobj.quantity:
                messages.error(request, "Order Quantity is more than Product Available Quantity !!!")
                form = OrderForm(request.POST or None)
                context = {
                    'form'      : form,
                    'product'    : product
                }
                return render(request, self.template_name, context)
            elif product.admin_approved=='Unapproved':
                messages.error(request, " Product is not approved by Admin !!!")
                form = OrderForm(request.POST or None)
                context = {
                    'form'      : form,
                    'product'    : product
                }
                return render(request, self.template_name, context)
            else:
                product.product_quantity -= orderobj.quantity   
                product.save()
                orderobj.save()
                messages.success(request, "New Order Created has been successfully !!!!")
                return redirect('customerpage')
        form = OrderForm(request.GET or None)
        context = {
            'form'      : form,
            'customer':customer,
        }
        return render(request, self.template_name, context)



# Customer Order Update

@login_required(login_url='customerlogin')
@allowed_users(allowed_groups=['customer'])
def updateorder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            orderobj = form.save(commit=False)
            product = get_object_or_404(Product, name=orderobj.product.name)
            if  product.product_quantity < orderobj.quantity:
                messages.error(request, "Order Quantity is more than Product Available Quantity !!!")
                form = OrderForm(request.POST or None)
                context = {
                    'form'      : form,
                    'product'    : product
                }
                return render(request, 'updateorder.html', context)
            else:
                product.product_quantity -= orderobj.quantity
                product.save()
                orderobj.save()
                messages.success(request, " Your Order has been updated successfully !!!!")
                return redirect('customerpage')
    context = {'form':form}
    return render(request, 'warehouse/updateorder.html', context)

# Customer Order Delete

@login_required(login_url='customerlogin')
@allowed_users(allowed_groups=['customer'])
def deleteorder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        product = get_object_or_404(Product, name=order.product.name)
        product.product_quantity += order.quantity
        product.save()
        order.delete()
        messages.success(request, " Your Order has been deleted successfully !!!!")
        return redirect('customerpage')
    context = {'order':order}
    return render(request, 'warehouse/deleteorder.html', context)


# Customer Deliveries list(admin approved only)

@login_required(login_url='customerlogin')
@allowed_users(allowed_groups=['customer'])
def orderdelivery(request):
    delivery= Delivery.objects.all()
    context={
       'delivery':delivery, 
    }
    return render(request, 'warehouse/delivery.html',context)

    
#Stock requested by admin Page

@login_required(login_url='supplierlogin')
@allowed_users(allowed_groups=['supplier'])
def stockreq(request):
    supplier=Supplier.objects.get(user_id=request.user.id)
    stockqs= StockRequest.objects.filter(supplier=request.user)
    form= StockRequestForm()
    if request.method == 'POST':
        form= StockRequestForm()
        if form.is_valid():
            form.save()
    else:
        form= StockRequestForm()
    context={
        'supplier':supplier,
        'stockqs':stockqs,
        'form':form
    }
    return render(request,'warehouse/stockreq.html',context)

    
#New Supplier Products Create

@login_required(login_url='supplierlogin')
@allowed_users(allowed_groups=['supplier'])
def createproduct(request,id):
    supplier=Supplier.objects.get(id=id)
    form=ProductForm(request.POST, supplier)
    if request.method =='POST':
        if form.is_valid():
            instance=form.save(commit=False)
            instance.supplier=supplier
            form.save()
            messages.success(request, f'New Product Created!!!')
            return redirect('supplierpage')
        else:
            print(form.errors)
    else:
        form = ProductForm()
    context={
        'form': form,

    }
    return render(request,"warehouse/createproducts.html",context)
