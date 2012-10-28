from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CompuClub_Site.views.home', name='home'),
    # url(r'^CompuClub_Site/', include('CompuClub_Site.foo.urls')),
    
    url(r'^fixtures/', include('fixtures.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', 'CompuClub_Site.views.home'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
