from django.conf.urls import patterns, url
from gallery.views import ImageList, ImageCreate

urlpatterns = patterns('',
   url(r'^$', ImageList.as_view(), name='list'),
   url(r'^upload/$', ImageCreate.as_view(), name='upload'),
)
