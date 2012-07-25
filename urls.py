from django.conf.urls.defaults import patterns, include, url
from testproject.views import hello, current_datetime,search_form,search
from testproject.views import inputs,thanks,download,process,dateedit
from testproject.views import processdate,edit,plot,start,redirect, mt_inputs
from testproject.views import mt_edit,mt_download,mt_process,mn_inputs, mn_edit
from testproject.views import mn_process,mn_download,am_inputs,am_edit,am_download,am_process
from testproject.views import mt_processdate,mn_processdate,am_processdate
from testproject.views import mt_dateedit,mn_dateedit,am_dateedit 
from django.contrib import admin # Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   (r'^app/$', start),
   (r'^app/hello/$', hello),
   (r'^app/redirect/$', redirect),
   (r'^app/time/$',current_datetime), 
   (r'^app/search-form/$',search_form),
   (r'^app/search/$',search),
   (r'^app/inputs/$',inputs),
   (r'^app/inputs/thanks/$',thanks),
   (r'^app/mt_inputs/$',mt_inputs),
   (r'^app/mt_inputs/thanks/$',thanks),
   (r'^app/mn_inputs/$',mn_inputs),
   (r'^app/mn_inputs/thanks/$',thanks),
   (r'^app/am_inputs/$',am_inputs),
   (r'^app/am_inputs/thanks/$',thanks),
   (r'^app/download/$',download),
   (r'^app/mt_download/$',mt_download),
   (r'^app/mn_download/$',mn_download),
   (r'^app/am_download/$',am_download),
   (r'^app/download/process/$',process),
   (r'^app/download/mt_process/$',mt_process),
   (r'^app/download/mn_process/$',mn_process),
   (r'^app/download/am_process/$',am_process),
   #(r'^app/download/process/$',plot),
   (r'^app/dateedit/$',dateedit),
   (r'^app/mt_dateedit/$',mt_dateedit),
   (r'^app/mn_dateedit/$',mn_dateedit),
   (r'^app/am_dateedit/$',am_dateedit),
   (r'^app/dateedit/processdate/$',processdate),
   (r'^app/mt_dateedit/mt_processdate/$',mt_processdate),
   (r'^app/mn_dateedit/mn_processdate/$',mn_processdate),
   (r'^app/am_dateedit/am_processdate/$',am_processdate),
   (r'^app/dateedit/processdate/(\d+)/edit/$',edit),
   (r'^app/dateedit/processdate/\d+/edit/thanks/$',thanks),
   (r'^app/mt_dateedit/mt_processdate/(\d+)/mt_edit/$',mt_edit),
   (r'^app/mt_dateedit/mt_processdate/\d+/mt_edit/thanks/$',thanks),
   (r'^app/mn_dateedit/mn_processdate/(\d+)/mn_edit/$',mn_edit),
   (r'^app/mn_dateedit/mn_processdate/\d+/mn_edit/thanks/$',thanks),
   (r'^app/am_dateedit/am_processdate/(\d+)/am_edit/$',am_edit),
   (r'^app/am_dateedit/am_processdate/\d+/am_edit/thanks/$',thanks),
   (r'^app/admin/',include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    # url(r'^testproject/', include('testproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
