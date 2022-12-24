from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Answer(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True) #updated_date can also be used to check if edited
    content = models.TextField()
    question_related = models.ForeignKey('forum.Question', on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):  
        return self.user.username

class Question(models.Model):
    # Fields for the question text and the date/time it was asked
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    updated_date = models.DateTimeField('date updated', auto_now=True)

    # Additional fields for storing additional information about the question
    # such as the user who asked it and any tags or categories it belongs to
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # tags = models.ManyToManyField(Tag)
    # category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    upvotes = models.PositiveIntegerField(default=0)
    answers = models.PositiveIntegerField(default=0)
    class Meta:
      #  models.UniqueConstraint(fields=['author','answers'],name='unique pair of author and answers')
        unique_together = [['author','answers']]
    def __str__(self):
        return f'{self.id}: {self.title}'
