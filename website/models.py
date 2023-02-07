from django.db import models
from datetime import date



class Grave(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True, blank=True)
    birth = models.DateField(null=False, default=date(2000, 1, 1))
    death = models.DateField(null=False, default=date(2000, 1, 1))
    veteran = models.CharField(max_length=10, null=True, blank=True)
    headstone =  models.CharField(max_length=10, null=True, blank=True)
    reference = models.CharField(max_length=10, null=True, blank=True)
    Grid = models.IntegerField(null=True, blank=True)
    Ward = models.IntegerField(null=True, blank=True)
    Block = models.IntegerField(null=True, blank=True)
    Lot = models.IntegerField(null=True, blank=True)
    Plot = models.IntegerField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "graves"
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name