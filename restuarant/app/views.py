from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    if request.method == 'GET':
        return render(request, 'html/index.html')

def menu(request):
    if request.method == 'GET':
        return render(request, 'html/menu.html')
    
def delivery(request):
    if request.method == 'GET':
        return render(request, 'html/delivery.html')
    
def reservation(request):
    if request.method == 'GET':
        return render(request, 'html/reservation.html')

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
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        time = request.POST.get('time')
        date = request.POST.get('date')
        comments = request.POST.get('comments')
        return render(request, 'result.html', {'name': name, 
                                               'phone': phone,
                                               'time': time,
                                               'date': date,
                                               'comments': comments
                                               })