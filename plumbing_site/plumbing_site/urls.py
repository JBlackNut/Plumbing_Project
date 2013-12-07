from django.conf.urls import patterns, include, url
from django.contrib import admin, auth
from product_exhibition.views import *
import product_exhibition
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'plumbing_site.views.home', name='home'),
    # url(r'^plumbing_site/', include('plumbing_site.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home_contact/', product_exhibition.views.home_contact, name = 'home_contact'),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': ''}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^home/', product_exhibition.views.home_page, name = "home_page"),
    url(r'^perspective/', product_exhibition.views.perspective, name = "perspective"),
    url(r'^product_list', product_exhibition.views.product_list, name = "product_list"),
    url(r'^product_detail/(?P<slug>[-\w]+)$', 'product_exhibition.views.product_detail', name = "product_detail"),
)
