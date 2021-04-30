from django.db import models

# Create your models here.
class source(models.Model):
    name = models.CharField(max_length=500,default='none')
    url = models.URLField(default='none')
    def __str__(self):
        return self.url
    
