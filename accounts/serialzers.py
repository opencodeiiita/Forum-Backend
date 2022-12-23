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
        return User.objects.create_user(**validated_data)