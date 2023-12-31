from django.shortcuts import render, redirect
from pizza.models import PizzaModel
from .models import OrderModel
from .forms import CreateForm, CreateOrderModelForm
from django.forms import modelformset_factory

# Create your views here.
def create_order(request, *args, **kwargs):
    all_pizzas = PizzaModel.objects.all()
    order_form = CreateForm(request.POST or None)

    if order_form.is_valid():
        address = order_form.cleaned_data.get('address')
        order = dict(order_form.data).get('choice')
        pizza = [PizzaModel.objects.get(pk = i) for i in order]
        new_order = OrderModel(address=address)
        new_order.save()
        new_order.pizza_order.add(*pizza)
        new_order.save()
        return redirect('createorder')
        
        # new_order = OrderModel.objects.create(address = address)
        # pizza = PizzaModel.objects.get(pk = order)
        # new_order.pizza_order.add(pizza)
        # new_order.save()
    
    context = {
        'pizzas': all_pizzas,
        'order_form': order_form
    }
    return render(request, 'order/create_order.html', context = context)

def create_model_order(request, *args, **kwargs):
    pizzas = PizzaModel.objects.all()
    model_form = CreateOrderModelForm(request.POST or None)
    # OrderFormSet = modelformset_factory(
    #     OrderModel,
    #     form=CreateOrderModelForm,
    #     extra=2)
    # model_form = OrderFormSet(
    #     request.POST or None,
    #     queryset=OrderModel.objects.none(),
    #     initial=[{
    #         'address': 'modelformset street'
    #     }])
    # if model_form.is_valid():
    #     model_form.save()
    #     return redirect('createmodelorder')
    context = {
        'pizzas': pizzas,
        'model_form': model_form,
    }
    return render(request, 'order/create_model_order.html', context=context)