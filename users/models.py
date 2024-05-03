from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries import Countries

# Create your models here.
class CustomUser(AbstractUser):
    username = models.CharField(max_length= 8, unique= True, blank = False, name = 'username')
    profile_pic = models.ImageField(upload_to= 'users/profile_picture/%Y', default= 'images/users/man_std.jpeg')
    country = Countries()
    friends = models.ManyToManyField(to='self',blank= True, symmetrical= True,default=None, related_name= 'friends')
    
