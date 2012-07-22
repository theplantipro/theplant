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

class Single_Main(models.Model):
   ph = models.DecimalField(max_digits=7,decimal_places=3)
   temp = models.DecimalField(max_digits=7,decimal_places=3)
   do = models.DecimalField(max_digits=7,decimal_places=3)
   nitrate = models.DecimalField(max_digits=7,decimal_places=3)

class Main_Testing(models.Model):
   system = models.IntegerField()
   date = models.DateField()
   author = models.CharField(max_length=50)
   tank1 = models.ForeignKey(Single_Main, related_name='main_testing_tank1')
   tank2 = models.ForeignKey(Single_Main, related_name='main_testing_tank2')
   tank3 = models.ForeignKey(Single_Main, related_name='main_testing_tank3')
   tank4 = models.ForeignKey(Single_Main, related_name='main_testing_tank4')
   sed = models.ForeignKey(Single_Main, related_name='main_testing_sed')
   beg = models.ForeignKey(Single_Main, related_name='main_testing_beg')
   end = models.ForeignKey(Single_Main, related_name='main_testing_end')
   note = models.CharField(max_length=1000)

   def __unicode__(self):
      return u'%s %s' % (self.author,self.date)

class Single_Nutrient(models.Model):
   reading = models.DecimalField(max_digits=7,decimal_places=3)
   actual = models.DecimalField(max_digits=7,decimal_places=3)

class Micro_Nutrient_Testing(models.Model):
   system = models.IntegerField()
   date = models.DateField()
   author = models.CharField(max_length=50)
   nitrate = models.ForeignKey(Single_Nutrient, related_name='micro_nutrient_nitrate')
   phosphorus = models.ForeignKey(Single_Nutrient, related_name='micro_nutrient_phosphorus')
   potassium = models.ForeignKey(Single_Nutrient, related_name='micro_nutrient_potassium')
   ammonia = models.ForeignKey(Single_Nutrient, related_name='micro_nutrient_ammonia')
   sulfate = models.ForeignKey(Single_Nutrient, related_name='micro_nutrient_sulfate')
   iron_actual = models.CharField(max_length=400)
   iron_reading = models.CharField(max_length=400)
   calcium = models.ForeignKey(Single_Nutrient, related_name='micro_nutrient_calcium')
   magnesium = models.ForeignKey(Single_Nutrient, related_name='micro_nutrient_magnesium')
   note = models.CharField(max_length=1000)

   def __unicode__(self):
      return u'%s %s' % (self.author,self.date)

class Ammonia_Nitrate(models.Model):
   tank1 = models.ForeignKey(Single_Nutrient, related_name='ammonia_nitrate_tank1')
   tank2 = models.ForeignKey(Single_Nutrient, related_name='ammonia_nitrate_tank2')
   tank3 = models.ForeignKey(Single_Nutrient, related_name='ammonia_nitrate_tank3')
   tank4 = models.ForeignKey(Single_Nutrient, related_name='ammonia_nitrate_tank4')
   sed = models.ForeignKey(Single_Nutrient, related_name='ammonia_nitrate_sed')
   beg = models.ForeignKey(Single_Nutrient, related_name='ammonia_nitrate_beg')
   end = models.ForeignKey(Single_Nutrient, related_name='ammonia_nitrate_end')

class Ammonia_Nitrate_Testing(models.Model):
   date = models.DateField()
   author = models.CharField(max_length=50)
   system = models.IntegerField()
   nitrate = models.ForeignKey(Ammonia_Nitrate, related_name='ammonia_nitrate_t__nit')
   ammonia = models.ForeignKey(Ammonia_Nitrate, related_name='ammonia_nitrate_t_am')
   note = models.CharField(max_length=1000)
   
   

