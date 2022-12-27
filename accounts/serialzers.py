from django.contrib.auth.models import User
from rest_framework import serializers
from accounts.models import Profile
import django.contrib.auth.password_validation as validators

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
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

       
class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        old_password = serializers.CharField(required = True,write_only = True)
        new_password = serializers.CharField(required = True,write_only = True)
        new_password_confirm = serializers.CharField(required = True,write_only = True)
        fields = '__all__'
        
        def validate(self,data):
            new_password = data['new_password']
            new_password_confirm = data['new_password_confirm']
            if new_password != new_password_confirm:
                raise serializers.ValidationError({'password':'passwords must match'})
            validators.validate_password(new_password)
            return data