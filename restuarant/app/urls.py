from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('delivery', views.delivery, name='delivery'),
    path('reservation', views.reservation, name='reservation'),
    path('form', views.form_submit, name='form_submit')
]