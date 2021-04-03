from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from rest_framework import status
from mypizzaapp.models import PizzaToppings,PizzaSize,MyPizzaStore
from mypizzaapp.serializers import PizzaSizeSerializer,PizzaToppingsSerializer,MyPizzaStoreSerializer
from mypizzaapp.filters import MyPizzaStoreFilter
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter 
from rest_framework import filters


class PizzaSizeViewSet(viewsets.ModelViewSet):
    queryset = PizzaSize.objects.all()
    serializer_class = PizzaSizeSerializer


class PizzaToppingViewSet(viewsets.ModelViewSet):
    queryset = PizzaToppings.objects.all()
    serializer_class = PizzaToppingsSerializer


class MyPizzaStoreViewSet(viewsets.ModelViewSet):
    queryset = MyPizzaStore.objects.all()
    serializer_class = MyPizzaStoreSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class =  MyPizzaStoreFilter

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            {
                'status' : 'success',
                'message': "Pizza order has been placed successfully.",
                'data' : serializer.data
            },status=status.HTTP_201_CREATED)  


    def perform_create(self,serializer):
        serializer.save()    

    def perform_update(self,serializer):
        serializer.save()  