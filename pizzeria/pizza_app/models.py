from django.db import models


class Pizza(models.Model):
    """ model that defines the pizza types"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Toppings(models.Model):
    """ model that defines the toppings for specific pizza"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name