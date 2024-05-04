from authentication.models import *
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# class UserSerializer(serializers.ModelSerializer):
#     id = serializers.UUIDField(read_only=True)
#     username = serializers.CharField(read_only=True)
#     image = serializers.ImageField(blank=True, null=True)
#     class Meta:
#         model = Users
#         fields = ['id','first_name', 'last_name' ,'username', 'email','phone_number','image']

from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class CustomUserCreateSerializer(UserCreateSerializer):
    id = serializers.UUIDField(read_only=True)
    username = serializers.CharField(read_only=True)
    image = serializers.ImageField(allow_empty_file=True)  # Remove the 'blank=True' argument

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'phone_number', 'image')

    def create(self, validated_data):
        # Set the username as the prefix of the email address
        validated_data['username'] = validated_data['email'].split('@')[0]
        return super().create(validated_data)

        
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        token['first_name'] = user.first_name
        token['email'] = user.email
        
        return token        
