from django.conf.urls import patterns, url, include, static
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('search.views',
    url(r'^$', 'login_view'),
    url(r'^login/$', 'login_view', name='login'),
    url(r'^dash$', 'dashboard', name='dash'),
    url(r'^list$', 'index', name='index'),
    url(r'^view/([0-9]+)/$', 'view', name='view'),
    url(r'^logout$', 'logout_view'),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^userprofile/', include('userprofile.urls', namespace="userprofile")),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)