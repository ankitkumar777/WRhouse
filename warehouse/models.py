from django.db import models

# Create your models here.
import datetime
from users.models import *

class Product(models.Model):
    Product_Approval=(('Unapproved','Unapproved'),( 'Approved','Approved'))
    Product_Category = (('Electronics','Electronics'),('Photography','Photography'),('Communication','Communication'),('Technology','Technology'),('Accessories','Accessories'),('Clothing','Clothing'),('Footwear','Footwear'),('Others','Others'))
    name = models.CharField(max_length=200)
    location= models.CharField(max_length=50)
    category = models.CharField(max_length=30, choices=Product_Category)
    brand = models.CharField(max_length=50)
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    admin_approved= models.CharField(max_length=50,default='Unapproved',choices=Product_Approval)
    product_quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    Order_Status= (('Pending','Pending'),('Processing','Processing'),('Declined','Declined'),('Approved','Approved'),)
    order_date = models.DateField(default=datetime.date.today, null = True) 
    product = models.ForeignKey(Product, on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(default=1)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=50, choices=Order_Status, default='Pending')

    def __str__(self):
        return str(self.product.name)+' '+ str(self.status)

class Delivery(models.Model):
    Delivery_Status=(('Pending','Pending'),('Shipped','Shipped'),('Delivered','Delivered'),)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    delivery_status = models.CharField(max_length=50, choices=Delivery_Status)
    delivered_Date = models.DateField(default=datetime.date.today, null = True)
    delievered_to = models.ForeignKey(Customer,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Deliveries"

    def __str__(self):
        return str(self.order.product.name)+' '+ str(self.delivery_status)

#****************Stock request added*********************

class StockRequest(models.Model):
    Order_Status= (('Pending','Pending'),('Processing','Processing'),('Declined','Declined'),('Delivered','Delivered'),)
    Product_Approval=(('Unapproved','Unapproved'),( 'Approved','Approved'))
    supplier = models.ForeignKey(User, on_delete=models.CASCADE,limit_choices_to={'groups__name': "supplier"})
    product = models.CharField(max_length=200)
    stock_qty= models.PositiveIntegerField(default=1)
    request_status = models.CharField(max_length=50, choices=Order_Status,default='Pending')
    created_at = models.DateField(auto_now=True, auto_now_add=False)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return str(self.product)+' '+ str(self.request_status)