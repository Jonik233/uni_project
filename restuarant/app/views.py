from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ReservationForm
from django.contrib import messages
from . import models

def home(request):
    if request.method == 'GET':
        return render(request, 'html/index.html')

def menu(request):
    if request.method == 'GET':
        dishes = models.Dish.objects.all()
        context = {"dishes": dishes, "length": len(dishes)}
        return render(request, 'html/menu.html', context)

def delivery(request):
    if request.method == 'GET':
        dishes = models.Dish.objects.all()
        context = {"dishes": dishes, "length": len(dishes)}
        return render(request, 'html/delivery.html', context)

def reservation(request):
    if request.method == 'GET':
        return render(request, 'html/reservation.html')

def error(request):
    if request.method == 'GET':
        return render(request, 'html/registration_response.html')
    
def get_connections(request):
    if request.method == 'GET':
        return render(request, 'html/communications.html')

def delivery_reg(request):
    if request.method == 'GET':
        return render(request, 'html/delivery_reg.html')

def delivery_review(request):
    if request.method == 'GET':
        return render(request, 'html/delivery_review.html')
    
def form_submit(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
             return redirect('error')
    else:                                              
        return render(request, 'html/reservation.html')
    