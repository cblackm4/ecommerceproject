from rest_framework import routers

from administration.views import (
    UserViewSet, GroupViewSet
)
from pawkages.views import (
    CustomerViewSet, ProductViewSet, IngredientViewSet,
    RecipeViewSet, SubscriptionViewSet, TransactionViewSet
)

ROUTER = routers.DefaultRouter()

ROUTER.register(r'users', UserViewSet)
ROUTER.register(r'groups', GroupViewSet)

ROUTER.register(r'customers', CustomerViewSet)
ROUTER.register(r'products', ProductViewSet)
ROUTER.register(r'ingredients', IngredientViewSet)
ROUTER.register(r'recipes', RecipeViewSet)
ROUTER.register(r'subscriptions', SubscriptionViewSet)
ROUTER.register(r'transactions', TransactionViewSet)
