from rest_framework import serializers

from .models import (
    Customer, Product, Ingredient,
    Recipe, Subscription, Transaction, Feedback
)

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):

    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe
        fields = ('id','user', 'pet_size', 'name', 'ingredients', 'description')
    
    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        recipe = Recipe.objects.create(**validated_data)
        ingredient_list = list()

        for ingredient in ingredients_data:
            ingredient_list.append(Ingredient.objects.get(name=ingredient.get('name')))

        recipe.ingredients.set(ingredient_list)
        recipe.save()

        return recipe

    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        new_name = validated_data.pop('name')
        new_description = validated_data.pop('description')
        new_pet_size = validated_data.pop('pet_size')

        ingredient_list = list()
        for ingredient in ingredients_data:
            ingredient_list.append(Ingredient.objects.get(name=ingredient.get('name')))

        instance.name = new_name
        instance.description = new_description
        instance.pet_size = new_pet_size
        instance.ingredients.set(ingredient_list)
        instance.save()

        return instance



class SubscriptionSerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True, read_only=True)
    recipes = RecipeSerializer(many=True, read_only=True)

    class Meta:
        model = Subscription
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
