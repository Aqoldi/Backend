from authentication.models import *
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = User
        fields = ['id','first_name', 'last_name' ,'username', 'email','phone_number','image']
        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        token['first_name'] = user.first_name
        token['username'] = user.username
        token['email'] = user.email
        token['image'] = str(user.image)
        
        return token        
    
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])   
    password2 = serializers.CharField(write_only=True, required=True)   
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email','phone_number','image', 'password', 'password2']
        
        
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError({'password': 'Passwords do not match'})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )    
        user.set_password(validated_data['password'])
        user.save()
        return user    