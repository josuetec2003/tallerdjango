from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('mapas.views',
    # Examples:
    url(r'^$', 'index', name='index'),
    url(r'^sistema/$', 'sistema', name='sistema'),
    url(r'^login/$', 'process_login', name='process_login'),
    url(r'^logout/$', 'process_logout', name='process_logout'),
    # url(r'^tallerdjango/', include('tallerdjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
