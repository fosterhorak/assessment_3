from django.db import models
#from django.urls import reverse

# Create your models here.

class Widget(models.Model):
    description = models.CharField(max_length=30)
    quantity = models.IntegerField()

    def __str__(self):
        return self.description
    
    # not sure if I'll need this yet...
    # def get_absolute_url(self):
    #     return reverse('index')