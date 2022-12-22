from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from forum.models import Answer, Question
from forum.serialzers import AnswerSerializer, QuestionSerializer
from django.shortcuts import get_object_or_404

from forum.models import Question

# Create your views here.

class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        serializer = AnswerSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save(user=request.user)
        resp_data = serializer.data
        question_id = get_object_or_404(Question, pk= request.data['question_related'])
        #updates question ID with question title in response
        resp_data['question_related'] = question_id.title
        return Response(resp_data, status=status.HTTP_201_CREATED)



class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        serializer = QuestionSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    