from django.conf.urls import patterns, url
from gallery.views import ImageList

urlpatterns = patterns('',
   url(r'^$', ImageList.as_view(), name='list'),
)
