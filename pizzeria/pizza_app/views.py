from django.shortcuts import render
from .models import Pizza


# Create your views here.
def index(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, r'pizza_app\index.html', context)

def pizza(request, id):
    try:
        pizza = Pizza.objects.get(id=id)
        toppings = pizza.toppings_set.all()
        context = {'pizza': pizza, 'toppings': toppings}
    except Exception:
        return render(request, r'pizza_app\index.html', {'pizzas': []})
    return render(request, r'pizza_app\pizza.html', context) 
