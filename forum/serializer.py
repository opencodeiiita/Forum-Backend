from rest_framework import serializers
from .models import Answer

class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Answer
        fields = ('user', 'created_at','updated_at', 'content', 'upvotes', 'downvotes')
