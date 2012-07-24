from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from data_log.models import Log,Single_Main,Main_Testing,Single_Nutrient
from data_log.models import Micro_Nutrient_Testing,Ammonia_Nitrate,Ammonia_Nitrate_Testing 
from django.core.context_processors import csrf
import datetime
import xlwt
import os
import numpy as np
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
      log.date = str(log.date)
    
      c.update({'mt':maint})
      return render_to_response('mt_edit.html',c)

   c.update({'errors':errors})
   return render_to_response('mt_input.html',c)

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
   

def getSingleMain(l):
   for i in xrange(len(l)):
      if not l[i] or l[i] == '':
         l[i] = -1
   sm = Single_Main(ph=l[0],temp=l[1],do=l[2],nitrate=l[3])
   sm.save()
   return sm

   

def thanks(request):
   c = {}
   c.update(csrf(request))
   return render_to_response('thanks.html',c)

def download(request):
   return render_to_response('download.html')

def process(request):
   errors=[]
   date1 = ''
   date2 = ''
   if request.method == 'GET':
      isAll = request.GET.get('alldates','')=='on' 
      if isAll:
         datetuple = getDates()
         date1 = datetuple[0]
         date2 = datetuple[1]
      date1s = request.GET.get('date1','')
      date2s = request.GET.get('date2','')
      action = request.GET.get('action')
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
      elif action == "main_testing": 
         objects = Main_Testing.objects.filter(date=date1)
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
   average = sum(y)/len(y)


   #fig = plt.figure()
   #ax = fig.add_subplot(1,1,1)

   ax.yaxis.set_major_formatter(FuncFormatter(lambda y,pos:('%.1f')%y))
   

   fig.autofmt_xdate()
   plt.scatter(x,y)
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

def filter_out(xy):
   if xy == '' or xy is None:
      return False
   try:
      return int(xy[1]) != -1
   except:
      return False

def getDates():
   first = Log.objects.all().order_by("date")[0]
   last = Log.objects.all().order_by("-date")[0]
   returnval = (first.date,last.date)
   return returnval

   
   
   
         
   
   

      
