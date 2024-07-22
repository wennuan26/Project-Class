from django.db import models

# Create your models here.
class Category (models.Model) :
    name = models.CharField(max_length = 20)
    def __str__(self) :
        return self.name
class Unit (models.Model) :
    name = models.CharField(max_length = 20)
    def __str__(self) :
        return self.name
class Item (models.Model) :
    name = models.CharField (max_length = 20)
    price = models.DecimalField(max_digits = 8, decimal_places = 2)
    image = models.ImageField(upload_to = 'items')
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete = models.CASCADE)
    def __str__(self):
        return self.name
    
class Supplier (models.Model) :
    name = models.CharField(max_length = 20)
    mobileno = models.CharField(max_length = 10)
    item = models.ManyToManyField(Item)

    def __str__(self):
        return self.name
    
class Order (models.Model):
    customer = models.CharField(max_length = 20)
    date = models.DateField()
    item = models.ManyToManyField(Item)

    def __str__(self):
        return self.customer
    
class Employee (models.Model) :
    name = models.CharField(max_length = 20)
    def __str__(self) :
        return self.name