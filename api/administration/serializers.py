from rest_framework import serializers

from django.contrib.auth.models import Group
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' # TODO restrict field visibility

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__' # TODO restrict field visibility
