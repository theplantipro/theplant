from django.conf.urls.defaults import patterns, include, url
from testproject.views import hello, current_datetime,search_form,search
from testproject.views import inputs,thanks,download,process,allobjects,dateedit
from testproject.views import processdate,edit,plot
from django.contrib import admin # Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   (r'^app/hello/$', hello),
   (r'^app/time/$',current_datetime), 
   (r'^app/search-form/$',search_form),
   (r'^app/search/$',search),
   (r'^app/inputs/$',inputs),
   (r'^app/inputs/thanks/$',thanks),
   (r'^app/download/$',download),
   (r'^app/download/process/$',process),
   #(r'^app/download/process/$',plot),
   (r'^app/download/allobjects/$',allobjects),
   (r'^app/dateedit/$',dateedit),
   (r'^app/dateedit/processdate/$',processdate),
   (r'^app/dateedit/processdate/(\d+)/edit/$',edit),
   (r'^app/dateedit/processdate/\d+/edit/thanks/$',thanks),
   (r'^app/admin/',include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    # url(r'^testproject/', include('testproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
