from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserProfile(models.Model):
  
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
      return self.user.username 
