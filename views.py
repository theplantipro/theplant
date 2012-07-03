from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from data_log.models import Log
from django.core.context_processors import csrf
import datetime

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
   errors=[]
   if request.method == 'POST':
      if not request.POST.get('date',''):
         errors.append('Enter a date')
      if not request.POST.get('sys1',''):
         errors.append('Enter for sys1')
      if not errors:
         l = Log(date=request.POST.get('date'),
               author=request.POST.get('author'),
               system1_food=request.POST.get('sys1'),
               system2_food=request.POST.get('sys2'),
               system3_food=request.POST.get('sys3'),
               system4_food=request.POST.get('sys4'),
               makeup_added=request.POST.get('makeup'),
               temp=request.POST.get('temp'),
               ph=request.POST.get('ph'),
               do=request.POST.get('do'),
               humidity=request.POST.get('humid'),
               note=request.POST.get('note'))
         l.save()
         return HttpResponseRedirect('/inputs/thanks/')
   return render_to_response('input.html',{'errors':errors})

def thanks(request):
   c = {}
   c.update(csrf(request))
   return render_to_response('thanks.html',c)

      
