
from django.urls import path
from mypizzaapp.views import MyPizzaStoreViewSet, PizzaSizeViewSet, PizzaToppingViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('mypizzastore',MyPizzaStoreViewSet)
router.register('pizzasize',PizzaSizeViewSet)
router.register('pizzatopping',PizzaToppingViewSet)


urlpatterns = [
    
    
] + router.urls