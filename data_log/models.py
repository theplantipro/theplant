from django.db import models

# Create your models here.
class Log(models.Model):
   date = models.DateField()
   author = models.CharField(max_length=50)
   system1_food = models.DecimalField(max_digits=7, decimal_places=3)
   system2_food = models.DecimalField(max_digits=7, decimal_places=3)
   system3_food = models.DecimalField(max_digits=7, decimal_places=3)
   system4_food = models.DecimalField(max_digits=7, decimal_places=3)
   makeup_added = models.CharField(max_length=200)
   temp = models.DecimalField(max_digits=6, decimal_places=3)
   ph = models.DecimalField(max_digits=5, decimal_places=3)
   do = models.DecimalField(max_digits=6, decimal_places=3)
   humidity = models.DecimalField(max_digits=6, decimal_places=3)
   note = models.CharField(max_length=1000)

   def __unicode__(self):
      return u'%s %s' % (self.author,self.date)
