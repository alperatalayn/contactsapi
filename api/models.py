from django.db import models
from django.conf import settings
from users.models import CustomUser



class Contact(models.Model):
    owner = models.ForeignKey(CustomUser, related_name='contacts', on_delete=models.CASCADE, null=True)
    first_name = models.CharField(default ="",max_length=50)
    last_name = models.CharField(default ="",max_length=50)
    phone = models.CharField(default ="",max_length=20)
    job =  models.CharField(default ="",max_length=50)

class Adress(models.Model):
    contact = models.ForeignKey(Contact, related_name='adresses', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)

    
