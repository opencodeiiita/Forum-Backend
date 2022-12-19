from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    #mapping to auth user model
    phone = models.IntegerField()
    age = models.IntegerField()
    photo = models.ImageField(upload_to='%Y/%m/', default = "default.png")
    gender = models.CharField(max_length=254)
    bio = RichTextField()               #about, Intersts & Hobbies
    skills = RichTextField()            #tech & otherwise

    def __str__(self):
        return self.user.username
