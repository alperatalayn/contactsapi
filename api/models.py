from django.db import models

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(default ="",max_length=50)
    last_name = models.CharField(default ="",max_length=50)
    phone = models.CharField(default ="",max_length=20)

    def __str__ (self):
        return self.first_name
