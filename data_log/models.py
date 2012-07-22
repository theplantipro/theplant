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

class Main_Testing(models.Model):
   system = models.IntegerField()
   date = models.DateField()
   author = models.CharField(max_length=50)
   tank1 = models.ForeignKey(Single_Main)
   tank2 = models.ForeignKey(Single_Main)
   tank3 = models.ForeignKey(Single_Main)
   tank4 = models.ForeignKey(Single_Main)
   sed = models.ForeignKey(Single_Main)
   beg = models.ForeignKey(Single_Main)
   end = models.ForeignKey(Single_Main)
   note = models.CharField(max_length=1000)

class Single_Main(models.Model):
   ph = models.DecimalField(max_digits=7,decimal_places=3)
   temp = models.DecimalField(max_digits=7,decimal_places=3)
   do = models.DecimalField(max_digits=7,decimal_places=3)
   nitrate = models.DecimalField(max_digits=7,decimal_places=3)

class Micro_Nutrient_Testing(models.Model):
   system = models.IntegerField()
   date = models.DateField()
   author = models.CharField(max_length=50)
   nitrate = models.ForeignKey(Single_Nutrient)
   phosphorus = models.ForeignKey(Single_Nutrient)
   potassium = models.ForeignKey(Single_Nutrient)
   ammonia = models.ForeignKey(Single_Nutrient)
   sulfate = models.ForeignKey(Single_Nutrient)
   iron_actual = models.CharField(max_length=400)
   iron_reading = models.CharField(max_length=400)
   calcium = models.ForeignKey(Single_Nutrient)
   magnesium = models.ForeignKey(Single_Nutrient)
   note = models.CharField(max_length=1000)

class Single_Nutrient(models.Model):
   reading = models.DecimalField(max_digits=7,decimal_places=3)
   actual = models.DecimalField(max_digits=7,decimal_places=3)

class Ammonia_Nitrate_Testing(models.Model):
   date = models.DateField()
   author = models.CharField(max_length=50)
   system = models.IntegerField()
   nitrate = models.ForeignKey(Ammonia_Nitrate)
   ammonia = models.ForeignKey(Ammonia_Nitrate)
   note = models.CharField(max_length=1000)
   
class Ammonia_Nitrate(models.Model):
   tank1 = models.ForeignKey(Single_Nutrient)
   tank2 = models.ForeignKey(Single_Nutrient)
   tank3 = models.ForeignKey(Single_Nutrient)
   tank4 = models.ForeignKey(Single_Nutrient)
   sed = models.ForeignKey(Single_Nutrient)
   beg = models.ForeignKey(Single_Nutrient)
   end = models.ForeignKey(Single_Nutrient)
   

