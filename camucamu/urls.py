from django.conf.urls.defaults import *
from views import *
from django.contrib import admin
admin.autodiscover()
from django.conf import settings
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
	(r'^$', home),
    (r'^home/$', home),
	(r'^stats/$', stats),  
	(r'^admin/', include(admin.site.urls)),
	(r'^search/$', search),
	(r'^contact/$', contact),
    (r'^contact/thanks/$', thanks),
    (r'^about/$', about),
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout),
    (r'^accounts/profile/$', profile),
    (r'^register/$', register),
    (r'^addbook/$', addbook),

    (r'^images/(?P<path>.*)$', 'django.views.static.serve',
             {'document_root': settings.MEDIA_ROOT}),
)

#(r'^admin/', include(admin.site.urls)),
#(r'^admin/doc/', include('django.contrib.admindocs.urls')),

# Examples:
# url(r'^$', 'camucamu.views.home', name='home'),
# url(r'^camucamu/', include('camucamu.foo.urls')),

# Uncomment the admin/doc line below to enable admin documentation:
# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

