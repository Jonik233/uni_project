from django.db import models

class ReservationProfile(models.Model):
    visitor_name = models.CharField(max_length=200)
    visitor_phone_number = models.IntegerField()
    date = models.DateField(auto_now_add=False)
    time = models.TimeField(auto_now_add=False)
    comments = models.TextField()

class Dish(models.Model):
    title = models.CharField(max_length=200)  
    description = models.TextField(max_length=500)
    weight = models.IntegerField()
    price = models.IntegerField()
    image_path = models.CharField(max_length=200)

