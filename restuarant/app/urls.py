from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('delivery', views.delivery, name='delivery'),
    path('reservation', views.reservation, name='reservation'),
    path('reservation_form', views.reservation_form, name='form_submit_reservation'),
    path('registration_form', views.delivery_form, name='form_submit_reg'),
    path('connection', views.get_connections, name='connection'),
    path('delivery_reg', views.delivery_reg, name='delivery_reg'),
    path('delivery_review', views.delivery_review, name='delivery_review'),
    path('error', views.error, name='error'),
    path('payment', views.payment, name='payment'),
    path('update_dish_quantity/', views.update_dish_quantity, name='update_dish_quantity')
]