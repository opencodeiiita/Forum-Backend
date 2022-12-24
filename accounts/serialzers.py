from django.contrib.auth.models import User
from rest_framework import serializers

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError('Email field cannot be blank')
        return value

    def create(self, validated_data):
        user = User()
        user.email = validated_data['email']
        user.username = validated_data['username']
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')