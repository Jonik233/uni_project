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
    
    CATEGORY_CHOICES = [
        ("appetizer", "Закуски"), 
        ("main", "Основні страви"),
        ("cheese", "Сири"),
        ("dessert", "Десерти"),
        ("beverages", "Напої")
    ]
    category = models.CharField(max_length=200, choices=CATEGORY_CHOICES)

class Order(models.Model):
    full_name = models.CharField(max_length=400, default="Default")
    address = models.CharField(max_length=200, default="Default")
    phone_number = models.IntegerField()
    comments = models.TextField(default="Default")
    quantities = models.JSONField()
    price = models.IntegerField(default=0)
    
    def update_quantities(self, new_quantities):
        self.quantities = new_quantities
        self.update_price(new_quantities)
        
    def update_price(self):
        dishes = Dish.objects
        self.price = sum([self.quantities[id] * dishes.get(id).price for id in self.quantities])

class Table(models.Model):
    number = models.IntegerField()
    booked = models.BooleanField()