from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class PurchaseSerializer(ModelSerializer):
    category_name = serializers.StringRelatedField(source='category', read_only=True)
    
    class Meta:
        model = Purchase
        fields = ('id', 'price', 'date', 'customer', 'category_name')
        
    def to_representation(self, instance):  
        representation = super().to_representation(instance)
        representation['category_name'] = instance.category.title
        return representation
    
    
class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


