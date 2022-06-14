from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField
    bio = models.TextField(blank=True)
    profileimg = CloudinaryField('image')
    
    def __str__(self):
        return self.user.username
    
