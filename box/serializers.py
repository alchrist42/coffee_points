from rest_framework import serializers
from .models import *

class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Order
        fields = ("coffee", "volume", "point", "customer", "comment", "created")



class CoffeeTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CoffeeType
        fields = ("id", "title")


class CoffeePointSerializer(serializers.ModelSerializer):
    coffee = CoffeeTypeSerializer(many=True, read_only=True)
    
    class Meta:
        model = CoffeePoint
        fields = ("id", "title", "place", "coffee")
