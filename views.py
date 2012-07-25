from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from data_log.models import Log,Single_Main,Main_Testing,Single_Nutrient
from data_log.models import Micro_Nutrient_Testing,Ammonia_Nitrate,Ammonia_Nitrate_Testing 
from django.core.context_processors import csrf
import datetime
import xlwt
import os,tempfile
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def hello(request):
    return HttpResponse("Hello world")

def start(request):
   return render_to_response('start.html')

def redirect(request):
   action = request.GET.get('action','') 
   redi = "../%s" % action 
   return HttpResponseRedirect(redi)
   

def current_datetime(request):
   now = datetime.datetime.now()
   return render_to_response('current_datetime.html',{'current_date',now})

def search_form(request):
   return render_to_response('search_form.html')

def search(request):
   if 'q' in request.GET:
      message = 'You searched for: %r' % request.GET['q']
   else:
      message = 'You submitted an empty form.'
   return HttpResponse(message)

def inputs(request):
   c = {}
   c.update(csrf(request))
   errors=[]
   if request.method == 'POST':
      author=request.POST.get('author','')
      date=request.POST.get('date','')
      system1_food=request.POST.get('sys1','') 
      system2_food=request.POST.get('sys2','')
      system3_food=request.POST.get('sys3','')
      system4_food=request.POST.get('sys4','')
      makeup_added=request.POST.get('makeup','')
      temp=request.POST.get('temp','')
      ph=request.POST.get('ph','')
      do=request.POST.get('do','')
      humidity=request.POST.get('humid','')
      note=request.POST.get('note','')

      if not date:
         errors.append('Enter a date')
      if not system1_food:
         system1_food = 0
      if not system2_food:
         system2_food = 0
      if not system3_food:
         system3_food = 0
      if not system4_food:
         system4_food = 0
      if not makeup_added:
         makeup_added = 0
      if not temp:
         temp = -1 
      if not ph:
         ph = -1 
      if not do:
         do = -1 
      if not humidity:
         humidity = -1 
      if not errors:
         l = Log(date=date,
               author=author,
               system1_food=system1_food,
               system2_food=system2_food,
               system3_food=system3_food,
               system4_food=system4_food,
               makeup_added=makeup_added,
               temp=temp,
               ph=ph,
               do=do,
               humidity=humidity,
               note=note)
         
         l.save()
         return HttpResponseRedirect('thanks/')
   c.update({'errors':errors})
   return render_to_response('input.html',c)

def mt_inputs(request):
   c = {}
   c.update(csrf(request))
   errors=[]
   if request.method == 'POST':
      date=request.POST.get('date','')
      if not date:
         errors.append('Enter a date')
      if not errors:
         author=request.POST.get('author','')
         system=request.POST.get('system','')
         tank1=getSingleMain(request.POST.getlist('tank1','')) 
         tank2=getSingleMain(request.POST.getlist('tank2','')) 
         tank3=getSingleMain(request.POST.getlist('tank3','')) 
         tank4=getSingleMain(request.POST.getlist('tank4','')) 
         sed=getSingleMain(request.POST.getlist('sed','')) 
         beg=getSingleMain(request.POST.getlist('beg','')) 
         end=getSingleMain(request.POST.getlist('end','')) 
         note=request.POST.get('note','')
         mt = Main_Testing(system=system,
                              date=date,
                              author=author,
                              tank1=tank1,
                              tank2=tank2,
                              tank3=tank3,
                              tank4=tank4,
                              sed=sed,
                              beg=beg,
                              end=end,
                              note=note)

         mt.save()
         return HttpResponseRedirect('thanks/')
   c.update({'errors':errors})
   return render_to_response('mt_input.html',c)

def mn_inputs(request):
   c = {}
   c.update(csrf(request))
   errors=[]
   if request.method == 'POST':
      date=request.POST.get('date','')
      if not date:
         errors.append('Enter a date')
      if not errors:
         author=request.POST.get('author','')
         system=request.POST.get('system','')
         nitrate=getSingleNutrient(request.POST.getlist('nitrate','')) 
         phosphorus=getSingleNutrient(request.POST.getlist('phosphorus','')) 
         potassium=getSingleNutrient(request.POST.getlist('potassium','')) 
         ammonia=getSingleNutrient(request.POST.getlist('ammonia','')) 
         sulfate=getSingleNutrient(request.POST.getlist('sulfate','')) 
         iron_reading=request.POST.get('iron_r','') 
         iron_actual=request.POST.get('iron_a','') 
         calcium=getSingleNutrient(request.POST.getlist('calcium','')) 
         magnesium=getSingleNutrient(request.POST.getlist('magnesium','')) 
         note=request.POST.get('note','')
         mnt = Micro_Nutrient_Testing(system=system,
                              date=date,
                              author=author,
                              nitrate=nitrate,
                              phosphorus=phosphorus,
                              potassium=potassium,
                              ammonia=ammonia,
                              sulfate=sulfate,
                              iron_reading=iron_reading,
                              iron_actual=iron_actual,
                              calcium=calcium,
                              magnesium=magnesium,
                              note=note)

         mnt.save()
         return HttpResponseRedirect('thanks/')
   c.update({'errors':errors})
   return render_to_response('mn_input.html',c)

def mt_edit(request,theid):
   c = {}
   c.update(csrf(request))
   errors=[]
   if request.method == 'POST':
      date=request.POST.get('date','')
      if not date:
         errors.append('Enter a date')
      if not errors:
         author=request.POST.get('author','')
         system=request.POST.get('system','')
         tank1=getSingleMain(request.POST.getlist('tank1','')) 
         tank2=getSingleMain(request.POST.getlist('tank2','')) 
         tank3=getSingleMain(request.POST.getlist('tank3','')) 
         tank4=getSingleMain(request.POST.getlist('tank4','')) 
         sed=getSingleMain(request.POST.getlist('sed','')) 
         beg=getSingleMain(request.POST.getlist('beg','')) 
         end=getSingleMain(request.POST.getlist('end','')) 
         note=request.POST.get('note','')

         mt  = Main_Testing.objects.filter(id=int(theid))[0]
         mt.author = author
         mt.system=system
         mt.date=date
         mt.tank1=tank1
         mt.tank2=tank2
         mt.tank3=tank3
         mt.tank4=tank4
         mt.sed=sed
         mt.beg=beg
         mt.end=end
         mt.note=note

         mt.save()
         return HttpResponseRedirect('thanks/')
   else:
      maint = Main_Testing.objects.filter(id=int(theid))[0]
      maint.tank1 = checkBlank(maint.tank1)
      maint.tank2 = checkBlank(maint.tank2)
      maint.tank3 = checkBlank(maint.tank3)
      maint.tank4 = checkBlank(maint.tank4)
      maint.sed = checkBlank(maint.sed)
      maint.beg = checkBlank(maint.beg)
      maint.end = checkBlank(maint.end)
      maint.date = str(maint.date)
    
      c.update({'mt':maint})
      return render_to_response('mt_edit.html',c)

   c.update({'errors':errors})
   return render_to_response('mt_input.html',c)

def mn_edit(request,theid):
   c = {}
   c.update(csrf(request))
   errors=[]
   if request.method == 'POST':
      date=request.POST.get('date','')
      if not date:
         errors.append('Enter a date')
      if not errors:
         author=request.POST.get('author','')
         system=request.POST.get('system','')
         nitrate=getSingleNutrient(request.POST.getlist('nitrate','')) 
         phosphorus=getSingleNutrient(request.POST.getlist('phosphorus','')) 
         potassium=getSingleNutrient(request.POST.getlist('potassium','')) 
         ammonia=getSingleNutrient(request.POST.getlist('ammonia','')) 
         sulfate=getSingleNutrient(request.POST.getlist('sulfate','')) 
         iron_reading=request.POST.get('iron_r','')
         iron_actual=request.POST.get('iron_a','')
         calcium=getSingleNutrient(request.POST.getlist('calcium','')) 
         magnesium=getSingleNutrient(request.POST.getlist('magnesium','')) 
         note=request.POST.get('note','')

         mn = Micro_Nutrient_Testing.objects.filter(id=int(theid))[0]
         mn.author = author
         mn.system=system
         mn.nitrate=nitrate
         mn.phosphorus=phosphorus
         mn.potassium=potassium
         mn.ammonia=ammonia
         mn.sulfate=sulfate
         mn.iron_reading=iron_reading
         mn.iron_actual=iron_actual
         mn.calcium=calcium
         mn.magnesium=magnesium
         mn.note=note
         mn.date=date

         mn.save()
         return HttpResponseRedirect('thanks/')
   else:
      micron = Micro_Nutrient_Testing.objects.filter(id=int(theid))[0]
      micron.nitrate = mn_checkBlank(micron.nitrate)
      micron.phosphorus = mn_checkBlank(micron.phosphorus)
      micron.potassium = mn_checkBlank(micron.potassium)
      micron.ammonia = mn_checkBlank(micron.ammonia)
      micron.sulfate = mn_checkBlank(micron.sulfate)
      micron.iron_actual = micron.iron_actual
      micron.iron_reading = micron.iron_reading
      micron.calcium = mn_checkBlank(micron.calcium)
      micron.magnesium = mn_checkBlank(micron.magnesium)
      micron.date = str(micron.date)
      micron.note = micron.note
      micron.author= micron.author
    
      c.update({'mn':micron})
      return render_to_response('mn_edit.html',c)

   c.update({'errors':errors})
   return render_to_response('mn_input.html',c)

def checkBlank(l):
   if l.ph== -1:
      l.ph= '' 
   if l.temp== -1:
      l.temp= '' 
   if l.do== -1:
      l.do = '' 
   if l.nitrate== -1:
      l.nitrate= '' 
   return l

def mn_checkBlank(l):
   if l.reading == -1:
      l.reading= '' 
   if l.actual == -1:
      l.actual = '' 
   return l
   

def getSingleMain(l):
   for i in xrange(len(l)):
      if not l[i] or l[i] == '':
         l[i] = -1
   sm = Single_Main(ph=l[0],temp=l[1],do=l[2],nitrate=l[3])
   sm.save()
   return sm

def getSingleNutrient(l):
   for i in xrange(len(l)):
      if not l[i] or l[i] == '':
         l[i] = -1
   sn = Single_Nutrient(reading=l[0],actual=l[1])
   sn.save()
   return sn

   

def thanks(request):
   c = {}
   c.update(csrf(request))
   return render_to_response('thanks.html',c)

def download(request):
   return render_to_response('download.html')

def mt_download(request):
   return render_to_response('mt_download.html')

def mn_download(request):
   return render_to_response('mn_download.html')

def process(request):
   errors=[]
   date1 = ''
   date2 = ''
   if request.method == 'GET':
      isAll = request.GET.get('alldates','')=='on' 
      action = request.GET.get('action')
      if isAll:
         datetuple = getDates(action)
         date1 = datetuple[0]
         date2 = datetuple[1]
      date1s = request.GET.get('date1','')
      date2s = request.GET.get('date2','')
      if not isAll and not date1s:
         errors.append('Enter a start date')
      if not isAll and not date2s:
         errors.append('Enter an end date')
      if isAll or (date1s and date2s): 
         if not isAll:
            date1 = datetime.datetime.strptime(date1s,"%Y-%m-%d")
            date2 = datetime.datetime.strptime(date2s,"%Y-%m-%d")
         if not isAll and date2<date1:
            errors.append('Starting date must be less or equal to ending date')
     
      if not errors:
         if action=="spreadsheet":
            write_to_spread(date1,date2)
            return HttpResponseRedirect('/static/admin/files/test.xls')
         elif action=="mt_spreadsheet":
            mt_write_to_spread(date1,date2)
            return HttpResponseRedirect('/static/admin/files/test.xls')
         else:
            if action=="temp":
               generate_plot(date1,date2,0)
            elif action=="ph":
               generate_plot(date1,date2,1)
            elif action=="do":
               generate_plot(date1,date2,2)
            elif action=="humidity":
               generate_plot(date1,date2,3)
            else:
               generate_plot(date1,date2,4)
            return HttpResponseRedirect('/static/admin/files/test.png')
 
def mt_process(request):
   errors=[]
   date1 = ''
   date2 = ''
   if request.method == 'GET':
      isAll = request.GET.get('alldates','')=='on' 
      export = request.GET.get('export','')=='on' 
      action = request.GET.get('action')
      system = request.GET.get('system')
      where = request.GET.get('where')
      thetype = request.GET.get('thetype')
      if isAll:
         datetuple = getDates("mt_spreadsheet")
         date1 = datetuple[0]
         date2 = datetuple[1]
      date1s = request.GET.get('date1','')
      date2s = request.GET.get('date2','')
      if not isAll and not date1s:
         errors.append('Enter a start date')
      if not isAll and not date2s:
         errors.append('Enter an end date')
      if isAll or (date1s and date2s): 
         if not isAll:
            date1 = datetime.datetime.strptime(date1s,"%Y-%m-%d")
            date2 = datetime.datetime.strptime(date2s,"%Y-%m-%d")
         if not isAll and date2<date1:
            errors.append('Starting date must be less or equal to ending date')
     
      if not errors:
         if export: 
            mt_write_to_spread(date1,date2)
            return HttpResponseRedirect('/static/admin/files/test.xls')
         else:
            mt_generate_plot(date1,date2,system,where,thetype)
            return HttpResponseRedirect('/static/admin/files/test.png')
 

   return render_to_response('download.html',{'errors':errors})

def mn_process(request):
   errors=[]
   date1 = ''
   date2 = ''
   if request.method == 'GET':
      isAll = request.GET.get('alldates','')=='on' 
      export = request.GET.get('export','')=='on' 
      action = request.GET.get('action')
      system = request.GET.get('system')
      thetype = request.GET.get('thetype')
      if isAll:
         datetuple = getDates("mn_spreadsheet")
         date1 = datetuple[0]
         date2 = datetuple[1]
      date1s = request.GET.get('date1','')
      date2s = request.GET.get('date2','')
      if not isAll and not date1s:
         errors.append('Enter a start date')
      if not isAll and not date2s:
         errors.append('Enter an end date')
      if isAll or (date1s and date2s): 
         if not isAll:
            date1 = datetime.datetime.strptime(date1s,"%Y-%m-%d")
            date2 = datetime.datetime.strptime(date2s,"%Y-%m-%d")
         if not isAll and date2<date1:
            errors.append('Starting date must be less or equal to ending date')
     
      if not errors:
         if export: 
            mn_write_to_spread(date1,date2)
            return HttpResponseRedirect('/static/admin/files/test.xls')
         else:
            mn_generate_plot(date1,date2,system,thetype)
            return HttpResponseRedirect('/static/admin/files/test.png')
 

   return render_to_response('download.html',{'errors':errors})


def dateedit(request):
   return render_to_response('dateedit.html')

def processdate(request):
   if request.method == 'GET':
      date1s = request.GET.get('date1','')
      action = request.GET.get('action','')
      date1 = datetime.datetime.strptime(date1s,"%Y-%m-%d")
      objects = []
      if action == "log": 
         objects = Log.objects.filter(date=date1)
         return render_to_response('processdate.html',{'date_list':objects})
      elif action == "main_testing": 
         objects = Main_Testing.objects.filter(date=date1)
         return render_to_response('mt_processdate.html',{'date_list':objects})
      elif action == "micro_nutrient_testing": 
         objects = Micro_Nutrient_Testing.objects.filter(date=date1)
         return render_to_response('mn_processdate.html',{'date_list':objects})
      return render_to_response('processdate.html',{'date_list':objects})

def edit(request,theid):
   c = {}
   c.update(csrf(request))
   errors=[]
   if request.method == 'POST':
      author=request.POST.get('author','')
      date=request.POST.get('date','')
      system1_food=request.POST.get('sys1','') 
      system2_food=request.POST.get('sys2','')
      system3_food=request.POST.get('sys3','')
      system4_food=request.POST.get('sys4','')
      makeup_added=request.POST.get('makeup','')
      temp=request.POST.get('temp','')
      ph=request.POST.get('ph','')
      do=request.POST.get('do','')
      humidity=request.POST.get('humid','')
      note=request.POST.get('note','')

      if not date:
         errors.append('Enter a date')
      if not system1_food:
         system1_food = 0
      if not system2_food:
         system2_food = 0
      if not system3_food:
         system3_food = 0
      if not system4_food:
         system4_food = 0
      if not makeup_added:
         makeup_added = 0
      if not temp:
         temp = -1 
      if not ph:
         ph = -1 
      if not do:
         do = -1 
      if not humidity:
         humidity = -1 
      if not errors:
         l = Log.objects.filter(id=int(theid))[0]
         l.author = author
         l.system1_food=system1_food
         l.system2_food=system2_food
         l.system3_food=system3_food
         l.system4_food=system4_food
         l.makeup_added=makeup_added
         l.temp=temp
         l.ph=ph
         l.do=do
         l.humidity=humidity
         l.note=note
            
         l.save()
         return HttpResponseRedirect('thanks/')
   else:
      log = Log.objects.filter(id=int(theid))[0]
      if log.temp == -1:
         log.temp = '' 
      if log.ph== -1:
         log.ph= '' 
      if log.do== -1:
         log.do = '' 
      if log.humidity== -1:
         log.humidity = '' 
      log.date = str(log.date)
    
      c.update({'log':log})
      return render_to_response('edit.html',c)
      
   c.update({'errors':errors})
   return render_to_response('edit.html',c)




   

   


def write_to_spread(date1,date2):
   objects = Log.objects.filter(date__gte=date1,date__lte=date2).order_by("date")
   path = '/srv/http/static/admin/files/test.xls'

   if os.path.exists(path):
      os.remove(path)
   
   wbk = xlwt.Workbook()
   sheet = wbk.add_sheet('sheet 1')
   sheet.write(0,0,'Date')
   sheet.write(0,1,'Name')
   sheet.write(0,2,'Sys1 (g)')
   sheet.write(0,3,'Sys2 (g)')
   sheet.write(0,4,'Sys3 (g)')
   sheet.write(0,5,'Sys4 (g)')
   sheet.write(0,6,'makeup')
   sheet.write(0,7,'temp (F)')
   sheet.write(0,8,'pH')
   sheet.write(0,9,'DO (mg)')
   sheet.write(0,10,'Humidity')
   sheet.write(0,11,'Note')
   i=1
   for obj in objects:
      sheet.write(i,0,obj.date.strftime('%m/%d/%Y'))
      sheet.write(i,1,obj.author)
      sheet.write(i,2,obj.system1_food)
      sheet.write(i,3,obj.system2_food)
      sheet.write(i,4,obj.system3_food)
      sheet.write(i,5,obj.system4_food)
      sheet.write(i,6,obj.makeup_added)
      sheet.write(i,7,'' if obj.temp == -1 else obj.temp)
      sheet.write(i,8,'' if obj.ph == -1 else obj.ph)
      sheet.write(i,9,'' if obj.do == -1 else obj.do)
      sheet.write(i,10,'' if obj.humidity == -1 else obj.humidity)
      sheet.write(i,11,obj.note)
      i=i+1
   wbk.save(path)

def mt_write_to_spread(date1,date2):
   objects = Main_Testing.objects.filter(date__gte=date1,date__lte=date2).order_by("date")
   path = '/srv/http/static/admin/files/test.xls'

   if os.path.exists(path):
      os.remove(path)
   
   wbk = xlwt.Workbook()
   sheet = wbk.add_sheet('sheet 1')
    
   i=0
   for obj in objects:
      sheet.write(i,0,'Date')
      sheet.write(i+1,0,'Name')
      sheet.write(i+3,0,'System')
      sheet.write(i+4,0,'Tank 1')
      sheet.write(i+5,0,'Tank 2')
      sheet.write(i+6,0,'Tank 3')
      sheet.write(i+7,0,'Tank 4')
      sheet.write(i+8,0,'Sediment Tank')
      sheet.write(i+9,0,'Beginning Bed')
      sheet.write(i+10,0,'End Bed')
      sheet.write(i+11,0,'Note')

      sheet.write(i+0,1,obj.date.strftime('%m/%d/%Y'))
      sheet.write(i+1,1,obj.author)
      sheet.write(i+2,1,'pH')
      sheet.write(i+2,2,'Temp (F)')
      sheet.write(i+2,3,'DO (mg/L)')
      sheet.write(i+2,4,'Nitrate (mg/L')
      sheet.write(i+3,1,obj.system)
      mt_write_row(i+4,1,obj.tank1,sheet)
      mt_write_row(i+5,1,obj.tank2,sheet)
      mt_write_row(i+6,1,obj.tank3,sheet)
      mt_write_row(i+7,1,obj.tank4,sheet)
      mt_write_row(i+8,1,obj.sed,sheet)
      mt_write_row(i+9,1,obj.beg,sheet)
      mt_write_row(i+10,1,obj.end,sheet)
      sheet.write(i+11,1,obj.note)
      i=i+13
      
   wbk.save(path)

def mt_write_row(row,column,obj,sheet):
   sheet.write(row,column,'' if obj.ph == -1 else obj.ph)
   sheet.write(row,column+1,'' if obj.temp == -1 else obj.temp)
   sheet.write(row,column+2,'' if obj.do == -1 else obj.do)
   sheet.write(row,column+3,'' if obj.nitrate == -1 else obj.nitrate)
   

def plot(request):
   errors=[]
   if request.method == 'GET':
      date1s = request.GET.get('date1','')
      date2s = request.GET.get('date2','')
      if not date1s:
         errors.append('Enter a start date')
      if not date2s:
         errors.append('Enter an end date')
      if date1s and date2s: 
         date1 = datetime.datetime.strptime(date1s,"%Y-%m-%d")
         date2 = datetime.datetime.strptime(date2s,"%Y-%m-%d")
         if date2<date1:
            errors.append('Starting date must be less or equal to ending date')
     
      if not errors:
         generate_plot(date1,date2,3)
         return HttpResponseRedirect('/static/admin/files/test.png')

   return render_to_response('download.html',{'errors':errors})

def generate_plot(date1,date2,thetype):
   path = '/srv/http/static/admin/files/test.png'
   if os.path.exists(path):
      os.remove(path)
   objects = Log.objects.filter(date__gte=date1,date__lte=date2).order_by("date")
   fig = plt.figure()
   ax = fig.add_subplot(1,1,1)
   ax.set_xlabel("Date",color='red')
   yaxis = []
   if thetype == 0:
      yaxis = [o.temp for o in objects]
      ax.set_ylabel("Temperature (F)",color='red')
      ax.set_title("Temperature Data")
   elif thetype == 1:
      yaxis = [o.ph for o in objects]
      ax.set_ylabel("ph",color='red')
      ax.set_title("ph Data")
   elif thetype == 2:
      yaxis = [o.do for o in objects]
      ax.set_ylabel("DO",color='red')
      ax.set_title("DO Data")
   elif thetype == 3:
      yaxis = [o.humidity for o in objects]
      ax.set_ylabel("Humidity",color='red')
      ax.set_title("Humidity Data")
   else:
      f1 = [o.system1_food for o in objects]
      f2 = [o.system2_food for o in objects]
      f3 = [o.system3_food for o in objects]
      f4 = [o.system4_food for o in objects]
      yaxis = [a+b+c+d for (a,b,c,d) in zip(f1,f2,f3,f4)]
      ax.set_ylabel("Total food for systems (g)",color='red')
      ax.set_title("Food Usage Data")



   dates = [o.date for o in objects]
   xy = zip(dates,yaxis)
   xy_filtered = xy 
   if thetype != 4:
      xy_filtered = filter(filter_out,xy)
   x = [temp[0] for temp in xy_filtered]
   y_temp = [temp[1] for temp in xy_filtered]
  
   y = map(parse_floats,y_temp)
   if(len(y) > 0):
      average = sum(y)/len(y)


   #fig = plt.figure()
   #ax = fig.add_subplot(1,1,1)

   ax.yaxis.set_major_formatter(FuncFormatter(lambda y,pos:('%.1f')%y))
   

   fig.autofmt_xdate()
   plt.scatter(x,y)
   txt = "No data points"
   if(len(y)>0):
      txt = "Average: %.1f" % average
   fig.text(1,0.95,txt,ha='right',va='top',transform=ax.transAxes,bbox=dict(facecolor='red',alpha=0.3))
   plt.savefig(path)

def mt_generate_plot(date1,date2,system,where,thetype):
   path = '/srv/http/static/admin/files/test.png'
   if os.path.exists(path):
      os.remove(path)
   objects = []
   tups = []
   if system == '3':
      objects = Main_Testing.objects.filter(date__gte=date1,date__lte=date2).order_by("date")
   else:
      objects = Main_Testing.objects.filter(date__gte=date1,date__lte=date2,system=system).order_by("date")

   if where=="tank1":
      tups = unzip([(o.tank1,o.date) for o in objects])   
   
   elif where=="tank2":
      tups = unzip([(o.tank2,o.date) for o in objects])   
   elif where=="tank3":
      tups = unzip([(o.tank3,o.date) for o in objects])   
   elif where=="tank4":
      tups = unzip([(o.tank4,o.date) for o in objects])   
   elif where=="sed":
      tups = unzip([(o.sed,o.date) for o in objects])   
   elif where=="beg":
      tups = unzip([(o.beg,o.date) for o in objects])  
   elif where=="end":
      tups = unzip([(o.end,o.date) for o in objects])   
   else:
      tupsy = []
      tupsy.extend([(o.tank1,o.date) for o in objects])
      tupsy.extend([(o.tank2,o.date) for o in objects])
      tupsy.extend([(o.tank3,o.date) for o in objects])
      tupsy.extend([(o.tank4,o.date) for o in objects])
      tupsy.extend([(o.sed,o.date) for o in objects])
      tupsy.extend([(o.beg,o.date) for o in objects])
      tupsy.extend([(o.end,o.date) for o in objects])
      tups = unzip([(tup[0],tup[1]) for tup in tupsy])
   dates = tups[1]
   objects = tups[0]

   fig = plt.figure()
   ax = fig.add_subplot(1,1,1)
   ax.set_xlabel("Date",color='red')
   yaxis = []
   if thetype == "temp":
      yaxis = [o.temp for o in objects]
      ax.set_ylabel("Temperature (F)",color='red')
   elif thetype == "ph":
      yaxis = [o.ph for o in objects]
      ax.set_ylabel("ph",color='red')
   elif thetype == "do":
      yaxis = [o.do for o in objects]
      ax.set_ylabel("DO (mg/L)",color='red')
      ax.set_title("DO Data")
   elif thetype == "nitrate":
      yaxis = [o.nitrate for o in objects]
      ax.set_ylabel("Nitrate (mg/L)",color='red')

   d = {'ph':'pH Data','do':'DO Data','nitrate':'Nitrate Data','temp':'Temperature Data','1':'System 1','2':'System 2','3':'System 1 and 2','tank1':'Tank 1','tank2':'Tank 2','tank3': 'Tank 3','tank4':'Tank 4','sed':'Sediment Tank','beg':'Beginning Bed','end':'End Bed','all':'All Tanks and Beds'}

   ax.set_title("%s for %s in %s" % (d[thetype],d[where],d[system]))

   #dates = [o.date for o in objects]
   xy = zip(dates,yaxis)
   xy_filtered = filter(filter_out,xy)
   x = [temp[0] for temp in xy_filtered]
   y_temp = [temp[1] for temp in xy_filtered]
  
   y = map(parse_floats,y_temp)
   if len(y) > 0:
      average = sum(y)/len(y)


   #fig = plt.figure()
   #ax = fig.add_subplot(1,1,1)

   ax.yaxis.set_major_formatter(FuncFormatter(lambda y,pos:('%.1f')%y))
   

   fig.autofmt_xdate()
   plt.scatter(x,y)
   txt = "No data points"
   if len(y) > 0:
      txt = "Average: %.1f" % average
   fig.text(1,0.95,txt,ha='right',va='top',transform=ax.transAxes,bbox=dict(facecolor='red',alpha=0.3))
   plt.savefig(path)

def parse_floats(string):
   if string is None:
      return 0
   if string is '':
      return 0
   try:
      return float(string)
   except:
      return 0

def mn_generate_plot(date1,date2,system,thetype):
   path = '/srv/http/static/admin/files/test.png'
   if os.path.exists(path):
      os.remove(path)
   tups = []
   objects = Micro_Nutrient_Testing.objects.filter(date__gte=date1,date__lte=date2,system=system).order_by("date")

   if thetype == "nitrate":
      tups = unzip([(o.nitrate,o.date) for o in objects])   
   elif thetype== "phosphorus":
      tups = unzip([(o.phosphorus,o.date) for o in objects])   
   elif thetype == "potassium":
      tups = unzip([(o.potassium,o.date) for o in objects])   
   elif thetype == "ammonia":
      tups = unzip([(o.ammonia,o.date) for o in objects])   
   elif thetype == "sulfate":
      tups = unzip([(o.sulfate,o.date) for o in objects])   
   elif thetype == "calcium":
      tups = unzip([(o.calcium,o.date) for o in objects])  
   elif thetype == "magnesium":
      tups = unzip([(o.magnesium,o.date) for o in objects])   

   dates = tups[1]
   objects = tups[0]

   fig = plt.figure()
   ax = fig.add_subplot(1,1,1)
   ax.set_xlabel("Date",color='red')
   yaxis_a = [o.actual for o in objects]
   yaxis_r = [o.reading for o in objects]
   ax.set_ylabel("ppm",color='red')

   d = {'nitrate':'Nitrate Data','phosphorus':'Phosphorus Data','potassium':'Potassium Data','ammonia':'Ammonia Data','sulfate':'Sulfate Data','calcium':'Calcium Data','magnesium':'Magnesium Data','1':'System 1','2':'System 2'}

   ax.set_title("%s for %s" % (d[thetype],d[system]))

   xy_a = zip(dates,yaxis_a)
   xy_r = zip(dates,yaxis_r)
   xy_filtered_a = filter(filter_out,xy_a)
   xy_filtered_r = filter(filter_out,xy_r)
   x_a = [temp[0] for temp in xy_filtered_a]
   x_r = [temp[0] for temp in xy_filtered_r]
   y_temp_a = [temp[1] for temp in xy_filtered_a]
   y_temp_r = [temp[1] for temp in xy_filtered_r]
  
   y_a = map(parse_floats,y_temp_a)
   y_r = map(parse_floats,y_temp_r)
   if len(y_a) > 0:
      average_a = sum(y_a)/len(y_a)
   if len(y_r) > 0:
      average_r = sum(y_r)/len(y_r)


   #fig = plt.figure()
   #ax = fig.add_subplot(1,1,1)

   ax.yaxis.set_major_formatter(FuncFormatter(lambda y_a,pos:('%.1f')%y_a))
   

   fig.autofmt_xdate()
   plt.plot(x_a,y_a)
   plt.plot(x_r,y_r)
   txt_a = "No data points"
   if len(y_a) > 0:
      txt_a = "Actual Average: %.1f" % average_a
   txt_r = "No data points"
   if len(y_r) > 0:
      txt_r = "Reading Average: %.1f" % average_r
   txt = "%s\n%s"%(txt_a,txt_r)
   fig.text(1,0.95,txt,ha='right',va='top',transform=ax.transAxes,bbox=dict(facecolor='red',alpha=0.3))
   plt.savefig(path)



def parse_floats(string):
   if string is None:
      return 0
   if string is '':
      return 0
   try:
      return float(string)
   except:
      return 0

def filter_out(xy):
   if xy == '' or xy is None:
      return False
   try:
      return int(xy[1]) != -1
   except:
      return False

def getDates(thetype):
   first=''
   last=''
   if(thetype=="spreadsheet"):
      first = Log.objects.all().order_by("date")[0]
      last = Log.objects.all().order_by("-date")[0]
   elif(thetype=="mt_spreadsheet"):
      first = Main_Testing.objects.all().order_by("date")[0]
      last = Main_Testing.objects.all().order_by("-date")[0]
   elif(thetype=="mn_spreadsheet"):
      first = Micro_Nutrient_Testing.objects.all().order_by("date")[0]
      last = Micro_Nutrient_Testing.objects.all().order_by("-date")[0]
   
   returnval = (first.date,last.date)
   return returnval

def unzip(seq):
   return zip(*seq)

   
   
   
         
   
   

      
