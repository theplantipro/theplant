from django.conf.urls.defaults import patterns, include, url
from testproject.views import hello, current_datetime,search_form,search
from testproject.views import inputs,thanks
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   (r'^test/hello/$', hello),
   (r'^test/time/$',current_datetime), 
   (r'^test/search-form/$',search_form),
   (r'^test/search/$',search),
   (r'^test/inputs/$',inputs),
   (r'^test/inputs/thanks/$',thanks),
   (r'^admin/',include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'testproject.views.home', name='home'),
    # url(r'^testproject/', include('testproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
