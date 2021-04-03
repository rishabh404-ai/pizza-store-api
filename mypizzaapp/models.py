from django.db import models

# Create your models here.


class PizzaSize(models.Model):
    size = models.CharField(max_length=100,null=True,blank=True) 

    def __str__(self):
        return self.size

class PizzaToppings(models.Model):
    topping = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.topping


class MyPizzaStore(models.Model):
    PIZZA_CHOICES = (
        ('Regular','Regular'),
        ('Square','Square'),
    )

    pizza_type = models.CharField(choices=PIZZA_CHOICES,max_length=8)
    pizza_size = models.ForeignKey(to=PizzaSize,on_delete=models.DO_NOTHING)
    pizza_toppings = models.ManyToManyField(to=PizzaToppings)

    def __str__(self):
        return self.pizza_type
    