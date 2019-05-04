from rest_framework import viewsets
from django.contrib.auth.models import Group
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import viewsets
from django.http import HttpResponse

from .models import (
    Customer, Product, Ingredient,
    Recipe, Subscription, Transaction, Feedback
)
from .serializers import (
    CustomerSerializer, ProductSerializer, IngredientSerializer,
    RecipeSerializer, SubscriptionSerializer, TransactionSerializer, FeedbackSerializer
)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

