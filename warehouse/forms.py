from warehouse.models import *
from django import forms

class OrderForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.all()
        self.fields['product'].widget.attrs.update({'class': 'textinput form-control ', 'required': 'true'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control ', 'min': '1', 'required': 'true'})
        self.fields['order_date'].widget.attrs.update({'class': 'dateinput form-control ', 'required': 'true'})
    class Meta:
        model = Order
        fields = '__all__'
        exclude=('customer','status')

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields =  '__all__'
        exclude=('admin_approved','supplier',)


class StockRequestForm(forms.ModelForm):
    class Meta:
        model= StockRequest
        fields=('request_status',)