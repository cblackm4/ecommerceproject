from django.db import models

from administration.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=125)
    billing_address = models.CharField(max_length=125)


class Product(models.Model):
    img_src = models.URLField()
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    price = models.FloatField()
    inventory = models.IntegerField()


class Ingredient(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=125)
    price = models.FloatField(default=0.0)



class Recipe(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, default = 'New Recipe')
    description = models.CharField(max_length=250, default = '')
    ingredients = models.ManyToManyField(Ingredient)
    PET_SIZE_CHOICES = (
        ('CAT', 'Cat'),
        ('SM', 'Small'),
        ('MD', 'Medium'),
        ('LG', 'Large'),
    )
    pet_size = models.CharField(max_length=3, choices=PET_SIZE_CHOICES, default='MD')


class Subscription(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(Recipe)
    products = models.ManyToManyField(Product)
    frequency = models.DurationField()
    active = models.BooleanField(default=True)


class Transaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    order_number = models.IntegerField()
    email = models.CharField(max_length=50)
    reason = models.CharField(max_length=250)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
