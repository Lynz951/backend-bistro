from .models import MenuItems, Diet, Category
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category']

class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = ['id', 'diet']

class MenuItemsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    diet = DietSerializer()
    class Meta:
        model = MenuItems
        fields = [
        'id', 
        'title', 
        'description', 
        'price',
        'category',
        'diet',
        ]
