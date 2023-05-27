from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu', views.menu, name='menu'),
    path('delivery', views.delivery, name='delivery'),
    path('reservation', views.reservation, name='reservation'),
    path('form', views.form_submit, name='form_submit'),
    path('connection', views.get_connections, name='connection'),
    path('delivery_reg', views.delivery_reg, name='delivery_reg'),
    path('delivery_review', views.delivery_review, name='delivery_review'),
    path('error', views.error, name='error')
]