from .models import *
from rest_framework.serializers import ModelSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class PurchaseSerializer(ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
        
class CustomerSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


