from django.contrib import admin
from .models import ReservationProfile, Dish, Order

admin.site.register(ReservationProfile)
admin.site.register(Dish)
admin.site.register(Order)