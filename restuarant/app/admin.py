from django.contrib import admin
from .models import ReservationProfile, Dish, Order, Table

admin.site.register(ReservationProfile)
admin.site.register(Dish)
admin.site.register(Order)
admin.site.register(Table)