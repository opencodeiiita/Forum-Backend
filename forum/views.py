from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView

from forum.models import Answer, Question

# Create your views here.

# class ListAnswer(ListView):

#     model = Answer

#     def get_queryset(self):
#         self.question = get_object_or_404(Question, name=self.kwargs['question'])
#         qs = super().get_queryset().filter(question_related=self.question).order_by("upvotes")
#         return qs