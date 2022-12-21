from rest_framework import serializers
from forum.models import Question

class QuestionSerialzers(serializers.ModelSerializer):
    #overriding author field to return author's name
    author = serializers.CharField(source='author.username')
    
    class Meta:
        model = Question
        fields = '__all__'