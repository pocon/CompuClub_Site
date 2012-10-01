from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fixtures.views.home', name='home'),
    # url(r'^fixtures/', include('fixtures.foo.urls')),

    url(r'^logout/^$', 'accounts.views.logout'),
    url(r'^login/^$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login.html'}),
    url(r'^register/^$', 'accounts.views.register'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
