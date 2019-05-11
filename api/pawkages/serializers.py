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

    def update(self, instance, validated_data):
        instance.inventory = validated_data.pop('inventory')
        instance.save()
        return instance


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

    products = ProductSerializer(many=True)
    recipes = RecipeSerializer(many=True)

    class Meta:
        model = Subscription
        fields = '__all__'

    def create(self, validated_data):
        recipe_data = validated_data.pop('recipes')
        product_data = validated_data.pop('products')

        subscription = Subscription.objects.create(**validated_data)

        recipe_list = list()
        product_list = list()

        for recipe in recipe_data:
            recipe_list.append(Recipe.objects.get(name=recipe.get('name')))

        for product in product_data:
            product_list.append(Product.objects.get(name=product.get('name')))

        subscription.recipes.set(recipe_list)
        subscription.products.set(product_list)
        subscription.save()

        return subscription

    def update(self, instance, validated_data):

        recipe_data = validated_data.pop('recipes')
        product_data = validated_data.pop('products')

        new_frequency = validated_data.pop('frequency')
        new_active = validated_data.pop('active')

        recipe_list = list()
        product_list = list()

        for recipe in recipe_data:
            recipe_list.append(Recipe.objects.get(name=recipe.get('name')))

        for product in product_data:
            product_list.append(Product.objects.get(name=product.get('name')))


        instance.recipes.set(recipe_list)
        instance.products.set(product_list)

        instance.frequency = new_frequency
        instance.active = new_active
        instance.save()

        return instance


class TransactionSerializer(serializers.ModelSerializer):

    products = ProductSerializer(many=True)
    recipes = RecipeSerializer(many=True)

    class Meta:
        model = Transaction
        fields = '__all__'

    def create(self, validated_data):
        recipe_data = validated_data.pop('recipes')
        product_data = validated_data.pop('products')

        transation = Transation.objects.create(**validated_data)

        recipe_list = list()
        product_list = list()

        for recipe in recipe_data:
            recipe_list.append(Recipe.objects.get(name=recipe.get('name')))

        for product in product_data:
            product_list.append(Product.objects.get(name=product.get('name')))

        transaction.recipes.set(recipe_list)
        transaction.products.set(product_list)
        transaction.save()

        return transaction


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'
