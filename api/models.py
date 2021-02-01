from django.db import models

class Contact(models.Model):
    id = models.AutoField(auto_created = True, 
                  primary_key = True, 
                  verbose_name ='ID'
                )
    first_name = models.CharField(default ="",max_length=50)
    last_name = models.CharField(default ="",max_length=50)
    phone = models.CharField(default ="",max_length=20)
    job =  models.CharField(default ="",max_length=50)

class Adress(models.Model):
    id = models.AutoField(auto_created = True, 
                  primary_key = True, 
                  verbose_name ='ID'
                )
    contact = models.ForeignKey(Contact, related_name='adresses', on_delete=models.CASCADE, default = "")
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)

    def __str__(self):
        return '%d: %s' % (self.title, self.content)

    
