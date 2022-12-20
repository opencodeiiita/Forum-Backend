from django.db import models

class Question(models.Model):
    # Fields for the question text and the date/time it was asked
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', add_now=True)
    updated_date = models.DateTimeField('date updated', auto_now=True)

    # Additional fields for storing additional information about the question
    # such as the user who asked it and any tags or categories it belongs to
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    upvotes = models.PositiveIntegerField(default=0)
    answers = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.id}: {self.title}'
