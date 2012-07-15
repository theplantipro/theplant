from django.db import models

# Create your models here.
class Log(models.Model):
   date = models.DateField()
   author = models.CharField(max_length=50,null=True)
   system1_food = models.DecimalField(max_digits=7, decimal_places=3)
   system2_food = models.DecimalField(max_digits=7, decimal_places=3)
   system3_food = models.DecimalField(max_digits=7, decimal_places=3)
   system4_food = models.DecimalField(max_digits=7, decimal_places=3)
   makeup_added = models.CharField(max_length=200)
   temp = models.DecimalField(max_digits=6, decimal_places=3,null=True)
   ph = models.DecimalField(max_digits=5, decimal_places=3,null=True)
   do = models.DecimalField(max_digits=6, decimal_places=3,null=True)
   humidity = models.DecimalField(max_digits=6, decimal_places=3,null=True)
   note = models.CharField(max_length=1000,null=True)
