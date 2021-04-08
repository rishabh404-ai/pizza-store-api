
from django.urls import path
from mypizzaapp.views import MyPizzaStoreViewSet, PizzaSizeViewSet, PizzaToppingViewSet, PizzaSizeGenericView, PizzaSizeGenericViewDetail
from rest_framework import routers

router = routers.DefaultRouter()
router.register('mypizzastore',MyPizzaStoreViewSet)
router.register('pizzasize',PizzaSizeViewSet)
router.register('pizzatopping',PizzaToppingViewSet)


urlpatterns = [
    path('pizza-size/',PizzaSizeGenericView.as_view()),
    path('pizza-size/<int:pk>/',PizzaSizeGenericViewDetail.as_view())
    
] + router.urls