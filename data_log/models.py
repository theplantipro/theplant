from django.db import models

# Create your models here.
class Log(models.Model):
   date = models.DateField()
   author = models.CharField(max_length=50)
   system1_food = models.DecimalField()
   system2_food = models.DecimalField()
   system3_food = models.DecimalField()
   system4_food = models.DecimalField()
   makeup_added = models.CharField(max_length=200)
   temp = models.DecimalField()
   ph = models.DecimalField()
   do = models.DecimalField()
   humidity = models.DecimalField()
   note = models.CharField(max_length=1000)
