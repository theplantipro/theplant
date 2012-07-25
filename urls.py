from django.conf.urls.defaults import patterns, include, url
from testproject.views import hello, current_datetime,search_form,search
from testproject.views import inputs,thanks,download,process,dateedit
from testproject.views import processdate,edit,plot,start,redirect, mt_inputs
from testproject.views import mt_edit,mt_download,mt_process,mn_inputs 
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
   (r'^app/download/$',download),
   (r'^app/mt_download/$',mt_download),
   (r'^app/download/process/$',process),
   (r'^app/download/mt_process/$',mt_process),
   #(r'^app/download/process/$',plot),
   (r'^app/dateedit/$',dateedit),
   (r'^app/dateedit/processdate/$',processdate),
   (r'^app/dateedit/processdate/(\d+)/edit/$',edit),
   (r'^app/dateedit/processdate/\d+/edit/thanks/$',thanks),
   (r'^app/dateedit/processdate/(\d+)/mt_edit/$',mt_edit),
   (r'^app/dateedit/processdate/\d+/mt_edit/thanks/$',thanks),
   (r'^app/admin/',include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    # url(r'^testproject/', include('testproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
