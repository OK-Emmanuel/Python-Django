from django.db import models

# Create your models here.
class Feature(models.Model):
    name =  models.CharField(max_length=100, default="Excellence")
    details = models.CharField(max_length=1000, default="we are creative and excellent team")
  
