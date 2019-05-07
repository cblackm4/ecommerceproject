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

    def get_queryset(self):
        """
        Only show recipes made by currently authenticated user.
        """
        user = self.request.user
        queryset = Recipe.objects.filter(user=user)
        return queryset


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        """
        Only show subscriptions for currently authenticated user.
        """
        user = self.request.user
        queryset = Subscription.objects.filter(user=user)
        return queryset


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_queryset(self):
        """
        Only show transaction history for currently authenticated user.
        """
        user = self.request.user
        queryset = Subscription.objects.filter(user=user)
        return queryset


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

