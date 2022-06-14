from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField
    bio = models.TextField(blank=True)
    profileimg = CloudinaryField('image')
    
    def __str__(self):
        return self.user.username
    
    
class Rating(models.Model):
    image = CloudinaryField('image')
    score = models.IntegerField(default=0,
                                validators=[
                                    MaxValueValidator(100),
                                    MinValueValidator(0)
                                            ]
                                )
    def __str__(self):
        return str(self.pk)