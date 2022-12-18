from django.db import models
import uuid

# Create your models here.
class Answer(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True) #updated_date can also be used to check if edited
    content = models.CharField(max_length=200)
    # question_related = models.ForeignKey(Question, on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)


    def __str__(self):  
        return str(self.id)