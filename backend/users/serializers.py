from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from api.models import Customer

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
        
    def create(self, clean_data):
        user_obj = UserModel.objects.create_user(email=clean_data['email'],
                                                 password=clean_data['password'],
                                                 username=clean_data['username'])
        user_obj.save()    
        customer = Customer.objects.create(name=clean_data['username'], email=clean_data['email'], password=clean_data['password'], user=user_obj)
        customer.save()
        return user_obj    
    
    
class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    
    def check_user(seld, clean_data):
        # user = authenticate(username=clean_data['email'], password=clean_data['password'])
        user = authenticate(username=clean_data['username'], password=clean_data['password'])
        if not user:
            print('asdkjfhsdalkjfhsklufhklsadfhkjlsadfhjkasdfhkjsdafhgas')
            raise serializers.ValidationError("user not found")
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('email', 'username')
        
