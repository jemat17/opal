from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from patients.views import IndexView, ContactView, schema_view

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view()),
    url(r'^contact/$', ContactView.as_view()),
    url(r'^schema/$', schema_view),
    url(r'^options/', include('options.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^patient/', include('patients.urls')),
)

urlpatterns += staticfiles_urlpatterns()
