import os
from io import BytesIO

from ckeditor.fields import RichTextField
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def gen_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

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

    def save(self, *args, **kwargs):
        pil_image = Image.open(self.photo)
        pil_image = pil_image.resize((300,300)) #resizing
        
        buffer = BytesIO()
        
        img_format = os.path.splitext(self.photo.name)[1][1:].upper() #to get the file type
        img_format = 'JPEG' if img_format == 'JPG' else img_format

        pil_image.save(fp=buffer, format=img_format)
        buffer = ContentFile(buffer.getvalue())
        self.photo = InMemoryUploadedFile(buffer,None, self.photo.name,'image/'+img_format.lower(),None, None)
        super(Profile, self).save(*args, **kwargs)
