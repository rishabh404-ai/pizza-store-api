from django.contrib import admin

from mypizzaapp.models import PizzaSize,PizzaToppings,MyPizzaStore

# Register your models here.
class PizzaSizeAdmin(admin.ModelAdmin):
    list_display = ('id','size')

admin.site.register(PizzaSize,PizzaSizeAdmin)

class PizzaToppingsAdmin(admin.ModelAdmin):
    list_display = ('id','topping')

admin.site.register(PizzaToppings,PizzaToppingsAdmin)

class MyPizzaStoreAdmin(admin.ModelAdmin):
    list_display = ('id','pizza_type','pizza_size','pizza_topping')

    def pizza_size(self,obj):
        return ",\n".join([sizes.size for sizes in obj.pizza_sizes.all()])
        
    def pizza_topping(self,obj):
        return ",\n".join([toppings.topping for toppings in obj.pizza_toppings.all()])      

admin.site.register(MyPizzaStore,MyPizzaStoreAdmin)
