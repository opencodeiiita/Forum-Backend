from rest_framework import serializers
from forum.models import Question, Answer

class QuestionSerialzer(serializers.ModelSerializer):
    #overriding author field to return author's name
    author = serializers.CharField(source='author.username')
    
    class Meta:
        model = Question
        fields = '__all__'
        
class AnswerSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username')

    class Meta:
        model = Answer
        fields = ('user', 'created_at','updated_at', 'content', 'upvotes', 'downvotes','question_related')