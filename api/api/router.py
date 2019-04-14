from rest_framework import routers
from administration.views import (UserViewSet, GroupViewSet)

ROUTER = routers.DefaultRouter()
ROUTER.register(r'users', UserViewSet)
ROUTER.register(r'groups', GroupViewSet)
