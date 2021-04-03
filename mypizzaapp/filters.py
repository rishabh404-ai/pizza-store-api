import django_filters
from django_filters import rest_framework as filters
from django_filters import FilterSet
from mypizzaapp.models import PizzaSize, PizzaToppings, MyPizzaStore
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

class MyPizzaStoreFilter(filters.FilterSet):
    pizza_size = filters.CharFilter(method='filter_by_pizza_size',label='pizza_size')
    pizza_type = filters.CharFilter(label='pizza_type')

    class Meta:
        model = MyPizzaStore
        fields = ['pizza_size','pizza_type']


    def filter_by_pizza_size(self,queryset,name,value):
        pizza_size = value
        size = PizzaSize.objects.filter(size=pizza_size)
        
        if PizzaSize.objects.filter(size=pizza_size).exists():
            return queryset.filter(pizza_size__in=size)
            
        else:
            raise ValidationError({'status': 'failed',
                                   'message':'Entered Pizza size not found',
                                   'data':[]}) 


