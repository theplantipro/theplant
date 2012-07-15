from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from data_log.models import Log
from django.core.context_processors import csrf
import datetime
import xlwt
import os

def hello(request):
    return HttpResponse("Hello world")

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

def thanks(request):
   c = {}
   c.update(csrf(request))
   return render_to_response('thanks.html',c)

def download(request):
   return render_to_response('download.html')

def process(request):
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
         write_to_spread(False,date1,date2)
         return HttpResponseRedirect('/static/admin/files/test.xls')

   return render_to_response('download.html',{'errors':errors})

def allobjects(request):
   write_to_spread(True)
   return HttpResponseRedirect('/static/admin/files/test.xls')

def dateedit(request):


def write_to_spread(isAll,date1=None,date2=None):
   if isAll:
      objects = Log.objects.all().order_by("date")
   else:
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
         
   
   

      
