from rest_framework import serializers
from mypizzaapp.models import PizzaSize,PizzaToppings,MyPizzaStore


class PizzaSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaSize
        fields = ['size']

class PizzaToppingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaToppings
        fields = ['topping']

class MyPizzaStoreSerializer(serializers.ModelSerializer):
    pizza_toppings = PizzaToppingsSerializer(many=True)
    pizza_size = serializers.SlugRelatedField(slug_field='size',queryset=PizzaSize.objects.all(),many=False)
    
    class Meta:
        model = MyPizzaStore
        fields = ['id','pizza_type','pizza_size','pizza_toppings']      
    
  
    def create(self, validated_data):
        toppings_data = validated_data.pop('pizza_toppings')

        pizza = MyPizzaStore.objects.create(**validated_data)

        for toppings in toppings_data:
            topping, created = PizzaToppings.objects.get_or_create(topping=toppings['topping'])   
            pizza.pizza_toppings.add(topping) 

        return pizza
      