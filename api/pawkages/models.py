from django.db import models

from administration.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    shipping_address = models.CharField(max_length=125)
    billing_address = models.CharField(max_length=125)


class Product(models.Model):
    img_src = models.URLField()
    name = models.CharField(max_length=250, default = 'Product')
    description = models.CharField(max_length=500, default = '')
    price = models.FloatField()
    inventory = models.IntegerField()


class Ingredient(models.Model):
    img_src = models.URLField(default='')
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=250)
    price = models.FloatField(default=0.0)



class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
    name = models.CharField(max_length=250, default = 'New Recipe')
    description = models.CharField(max_length=500, default = '')
    ingredients = models.ManyToManyField(Ingredient)
    PET_SIZE_CHOICES = (
        ('CAT', 'Cat'),
        ('SM', 'Small'),
        ('MD', 'Medium'),
        ('LG', 'Large'),
    )
    pet_size = models.CharField(max_length=3, choices=PET_SIZE_CHOICES, default='MD')


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    recipes = models.ManyToManyField(Recipe)
    products = models.ManyToManyField(Product)
    frequency = models.DurationField()
    active = models.BooleanField(default=True)


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    products = models.ManyToManyField(Product)
    date = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    order_number = models.IntegerField()
    email = models.CharField(max_length=50)
    reason = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date = models.DateTimeField(auto_now_add=True)
