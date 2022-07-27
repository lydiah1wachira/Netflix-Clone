from django.db import models

# Create your models here.
class Profile(models.Model):
    '''
    User model class to help create new user objects
    '''
    first_name = models.CharField(max_length=30)
    bio = models
    
