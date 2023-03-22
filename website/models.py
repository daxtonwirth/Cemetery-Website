from django.db import models
from datetime import date


class Grave(models.Model):

    Grid = models.TextField(null=True)

    Ward = models.TextField(null=True)
    Block = models.TextField(null=True)
    Lot = models.TextField(null=True)
       
    Occupant = models.TextField(null=True)
       
    Veteran = models.TextField(null=True)
    Headstone =  models.TextField(null=True)
    
    Birth = models.TextField() #DateField(null=False, default=date(2000, 1, 1))
    Death = models.TextField() #DateField(null=False, default=date(2000, 1, 1))
    
    
    class Meta:
        verbose_name_plural = "graves"
    
    def __str__(self):
        return self.Occupant