from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def checkout(request):
        quantity_from_form = int(request.POST["quantity"])
        price_from_form = float(request.POST["price"])
        total_charge = quantity_from_form * price_from_form


        if 'total_price' not in request.session:
            request.session['total_price'] = total_charge
        else:
            request.session['total_price'] =request.session['total_price'] +total_charge

        if 'quantity_ordered' not in request.session:
            request.session['quantity_ordered'] = quantity_from_form
        else:
            request.session['quantity_ordered'] =request.session['quantity_ordered'] +quantity_from_form

        print("Charging credit card...")
        Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
        return redirect('chre')

def chre(request):
    quantity_ordered = request.session.get('quantity_ordered')
    total_price = request.session.get('total_price')
    price_from_form = request.session.get('price_from_form')

    context = {
        'quantity_ordered': quantity_ordered,
        'total_price': total_price,
        'price_from_form': price_from_form
    }
    return render(request, "store/checkout.html", context)

def delete(request):
    del request.session['total_price']
    del request.session['quantity_ordered']

    return redirect('index')






