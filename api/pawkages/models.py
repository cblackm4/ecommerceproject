from django.db import models

from administration.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=125)
    billing_address = models.CharField(max_length=125)


class Product(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=125)
    price = models.FloatField()
    inventory = models.IntegerField()


class Ingredient(models.Model):
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=125)
    price = models.FloatField(default=0.0)


class Recipe(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
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
