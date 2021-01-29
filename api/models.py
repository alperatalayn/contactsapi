from django.db import models

class Contact(models.Model):
    first_name = models.CharField(default ="",max_length=50)
    last_name = models.CharField(default ="",max_length=50)
    phone = models.CharField(default ="",max_length=20)
    job =  models.CharField(default ="",max_length=50)

class Adress(models.Model):
    contact = models.ForeignKey(Contact, related_name='adresses', on_delete=models.CASCADE, default = "")
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)

    def __str__(self):
        return '%d: %s' % (self.title, self.content)

    
