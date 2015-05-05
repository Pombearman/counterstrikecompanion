from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yrs2k15_2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('csc.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
