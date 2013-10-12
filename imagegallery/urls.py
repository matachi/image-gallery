from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
import gallery

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'imagegallery.views.home', name='home'),
    # url(r'^imagegallery/', include('imagegallery.foo.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^gallery/', include('gallery.urls', namespace='gallery')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
