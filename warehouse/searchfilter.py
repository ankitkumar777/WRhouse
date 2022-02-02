import django_filters
from warehouse.models import Product

class ProductFilter(django_filters.FilterSet):
	name = django_filters.CharFilter(field_name='name',lookup_expr='icontains')
	location= django_filters.CharFilter(lookup_expr='icontains')
	brand= django_filters.CharFilter(lookup_expr='icontains')

	class Meta:
		model = Product
		fields = '__all__'
		exclude = ('product_quantity',)