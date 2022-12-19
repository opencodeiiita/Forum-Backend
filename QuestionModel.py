from django.db import models

class Question(models.Model):
    # Fields for the question text and the date/time it was asked
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # Additional fields for storing additional information about the question
    # such as the user who asked it and any tags or categories it belongs to
    asked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
