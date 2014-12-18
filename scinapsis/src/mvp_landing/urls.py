from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'signups.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
     url(r'^privacy-statement/$', 'signups.views.privacy', name='privacy'),
     url(r'^blog/$', 'signups.views.blog', name='blog'),
    url(r'^contact/$', 'signups.views.contact', name='contact'),
    url(r'^coming-soon/$', 'signups.views.comingsoon', name='comingsoon'),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                            document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                             document_root=settings.MEDIA_ROOT)