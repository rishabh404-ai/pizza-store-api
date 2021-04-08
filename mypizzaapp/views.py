from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from rest_framework import status
from mypizzaapp.models import PizzaToppings,PizzaSize,MyPizzaStore
from mypizzaapp.serializers import PizzaSizeSerializer,PizzaToppingsSerializer,MyPizzaStoreSerializer
from mypizzaapp.filters import MyPizzaStoreFilter
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter 
from rest_framework import filters
from django.http import Http404

class PizzaSizeViewSet(viewsets.ModelViewSet):
    queryset = PizzaSize.objects.all()
    serializer_class = PizzaSizeSerializer

class PizzaSizeGenericView(generics.GenericAPIView):
    """
    List all sizes, or create a new size.
    """

    serializer_class = PizzaSizeSerializer
    queryset = PizzaSize.objects.all()

    def get(self,request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = PizzaSizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status' : 'success',
                'message': "Pizza size has been added successfully.",
                'data' : serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response({
                'status' : 'success',
                'message': serializer.errors,
                'data' : []
            }, status=status.HTTP_400_BAD_REQUEST)


class PizzaSizeGenericViewDetail(generics.GenericAPIView):
    """
    Retrieve, update or delete a size instance.
    """
    serializer_class = PizzaSizeSerializer

    def get_object(self, pk):
        try:
            return PizzaSize.objects.get(pk=pk)
        except PizzaSize.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        size = self.get_object(pk)
        serializer = PizzaSizeSerializer(size)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        size = self.get_object(pk)
        serializer = PizzaSizeSerializer(size, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        size = self.get_object(pk)
        size.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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