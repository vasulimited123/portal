from django.db import models
from django.contrib.auth.models import User



class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    auth_token = models.CharField(max_length = 100, blank = True, null= True)
    phone = models.CharField(max_length = 10,  blank = True, null= True)
    address = models.TextField( blank = True, null= True)
    
    
