from .models import MenuItems, Diet, Category
from rest_framework import serializers


class MenuItemsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MenuItems
        fields = [
        'id', 
        'title', 
        'description', 
        'price',
        ]


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']