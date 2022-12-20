from rest_framework import serializers
from forum.models import Question

class QuestionSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fiels = '__all__'