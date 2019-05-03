from rest_framework import serializers

from django.contrib.auth.models import Group
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff')

    def update(self, instance, validated_data):
        if instance.email != validated_data.pop('email'): # The email is being changed
            pass #TODO send verification email
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__' # TODO restrict field visibility
