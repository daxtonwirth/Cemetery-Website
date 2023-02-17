from django.db import models
from datetime import date



class Grave(models.Model):
    #Reference = models.TextField(null=True) #CharField(max_length=10, null=True, blank=True)
    #Column = models.TextField(null=True)
    #Row = models.TextField(null=True) #CharField(max_length=10, null=True, blank=True)
    #Grid = models.TextField(null=True) #IntegerField(null=True, blank=True)
    
    #Ward = models.IntegerField(null=True, blank=True)
    #Block = models.IntegerField(null=True, blank=True)
    #Lot = models.IntegerField(null=True, blank=True)
    
    #Plot = models.TextField(null=True)
    
    Veteran = models.TextField(null=True)
    #Headstone =  models.TextField(null=True)
    
    Birth = models.TextField() #DateField(null=False, default=date(2000, 1, 1))
    Death = models.TextField() #DateField(null=False, default=date(2000, 1, 1))
    
    FirstName = models.TextField(null=True)
    LastName = models.TextField(null=True)
    #middle_name = models.CharField(max_length=30, null=True, blank=True)
    
    
    class Meta:
        verbose_name_plural = "graves"
    
    def __str__(self):
        return self.FirstName + ' ' + self.LastName