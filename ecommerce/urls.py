from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ecommerce.views.home', name='home'),
    # url(r'^blog/', include('blog.urls'))
    url(r'^$', 'home.views.index', name='index'),
    url(r'^shops', include('shops.urls')),
    #url(r'^$', include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),
   # url(r'^ecommerce/', include('ecommerce.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
                 {'document_root': settings.MEDIA_ROOT}),
   # url(r"^payments/", include("payments.urls")),
)
