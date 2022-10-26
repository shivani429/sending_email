from django.db import models
from datetime import datetime

class Emp(models.Model):
    Empcode = models.IntegerField()
    Name = models.CharField(max_length=50)
    DOBirth = models.DateField(max_length=50)
    DOJoining = models.DateField(max_length=50)
    DOAnniversary = models.DateField(max_length=50)
    Email = models.EmailField(max_length=50)

    def __str__(self):
        return self.Name
    
  





