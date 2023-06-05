from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import ReservationForm, OrderForm
from django.contrib import messages
from . import models
from django.core.exceptions import ObjectDoesNotExist
import json 

def home(request):
    if request.method == 'GET':
        request.session.flush()
        return render(request, 'html/index.html')

def menu(request, category):
    if request.method == 'GET':
        request.session.flush()
        context = menu_category(category)
        context['active_category'] = category
        return render(request, 'html/menu.html',context)

def delivery(request):
    if request.method == 'GET':
        dishes = models.Dish.objects.all()
        context = {"dishes": dishes, "length": len(dishes)}
        request.session.flush()
        return render(request, 'html/delivery.html', context)

def update_dish_quantity(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        dish_id = data.get('dish_id')
        quantity = data.get('quantity')

        if 'quantities' not in request.session:
            request.session['quantities'] = {str(dish_id): quantity}
        else:
            request.session['quantities'][str(dish_id)] = quantity

        request.session.save()
        # Return a JSON response indicating success
        return JsonResponse({'status': 'success'})

    # Return an error response if the request is not valid
    return JsonResponse({'status': 'error'}, status=400)


def reservation(request):
    if request.method == 'GET':
        request.session.flush()
        return render(request, 'html/reservation.html')

def error(request):
    if request.method == 'GET':
        return render(request, 'html/registration_response.html')

def get_connections(request):
    if request.method == 'GET':
        return render(request, 'html/communications.html')

def delivery_reg(request):
    if request.method == 'GET':
        quantities = request.session.get('quantities', {})
        dishes = models.Dish.objects
        price = sum([quantities[id] * dishes.get(id=id).price for id in quantities])
        context = {'price': price}
        return render(request, 'html/delivery_reg.html', context)

def delivery_review(request):
    if request.method == 'GET':
        quantities = request.session.get("quantities", {})
        menu = models.Dish.objects
        dishes = [menu.get(id=id) for id in quantities]
        quantities = [quantities[id] for id in quantities]
        context = {"quantities": quantities, "dishes": dishes}
        return render(request, 'html/delivery_review.html', context)

def reservation_form(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
             return redirect('error')
    else:                                              
        return render(request, 'html/reservation.html')

def delivery_form(request):
    if request.method == 'POST':
        post_data = request.POST.copy()
        quantities = request.session.get('quantities')
        dishes = models.Dish.objects
        price = sum([quantities[id] * dishes.get(id=id).price for id in quantities])
        post_data["quantities"] = quantities
        post_data["price"] = price
               
        form = OrderForm(post_data or None)
        if form.is_valid():
            form.save()
            return redirect('payment')
        else:
             return redirect('error')
    else:                                              
        return render(request, 'html/delivery_reg.html')    

def payment(request):
    if request.method == 'GET':
        return render(request, 'html/payment.html')
    
def menu_category(category):

    dishes = models.Dish.objects.filter(category=category)

    menu_data = []
    for dish in dishes:
        menu_data.append({
            'image_path': dish.image_path,
            'title': dish.title,
            'description': dish.description,
            'weight': dish.weight,
            'price': dish.price,
        })
    context = {"dishes":menu_data, "selected_category": category}
    return context