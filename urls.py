from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('mapas.views',
    # Examples:
    url(r'^$', 'index', name='index'),
    url(r'^sistema/$', 'sistema', name='sistema'),
    url(r'^login/$', 'process_login', name='process_login'),
    url(r'^logout/$', 'process_logout', name='process_logout'),
    url(r'^sistema/ubicacion/add$', 'agregar_ubicacion', name='agregar_ubicacion'),
    url(r'^sistema/mis_ubicaciones/$', 'mis_ubicaciones', name='mis_ubicaciones'),
    # url(r'^tallerdjango/', include('tallerdjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),    
    
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
   )
