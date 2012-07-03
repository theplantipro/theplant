from django.template.loader import get_template
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("Hello world")

def current_datetime(request):
   now = datetime.datetime.now()
   return render_to_response('current_datetime.html',{'current_date',now}} 
