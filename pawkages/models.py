from django.db import models

from administration.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    shipping_address = models.CharField(max_length=256)
    billing_address = models.CharField(max_length=256)


class Product(models.Model):
    img_src = models.URLField()
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    price = models.FloatField()
    inventory = models.IntegerField()


class Ingredient(models.Model):
    img_src = models.URLField(default='')
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    price = models.FloatField(default=0.0)



class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, default='New Recipe')
    description = models.CharField(max_length=512, default='')
    ingredients = models.ManyToManyField(Ingredient)
    PET_SIZE_CHOICES = (
        ('CAT', 'Cat'),
        ('SM', 'Small'),
        ('MD', 'Medium'),
        ('LG', 'Large'),
    )
    pet_size = models.CharField(max_length=3, choices=PET_SIZE_CHOICES, default='MD')


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(Recipe)
    products = models.ManyToManyField(Product)
    frequency = models.DurationField()
    active = models.BooleanField(default=True)


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    recipes = models.ManyToManyField(Recipe)
    date = models.DateTimeField(auto_now_add=True)


class Feedback(models.Model):
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    order_number = models.IntegerField()
    email = models.CharField(max_length=64)
    reason = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
