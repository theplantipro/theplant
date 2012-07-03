from django.db import models

# Create your models here.
class Log(models.Model):
   date = DateField()
   author = CharField(max_length=50)
   system1_food = DecimalField()
   system2_food = DecimalField()
   system3_food = DecimalField()
   system4_food = DecimalField()
   makeup_added = CharField(max_length=200)
   temp = DecimalField()
   ph = DecimalField()
   do = DecomalField()
   humidity = DecomalField()
   note = CharField(max_length=1000)
