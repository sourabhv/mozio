from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^provider/$', views.provider, name='provider'),
    url(r'^provider/(?P<provider_id>[0-9]+)/$', views.provider, name='provider'),
    url(r'^provider/(?P<provider_id>[0-9]+)/area/$', views.provider_area, name='provider_area'),
    url(r'^provider/(?P<provider_id>[0-9]+)/area/(?P<area_id>[0-9]+)/$', views.provider_area, name='provider_area'),
    url(r'^provider/(?P<provider_id>[0-9]+)/area/query/$', views.provider_area_query, name='provider_area_query'),

    url(r'^area/$', views.area, name='area'),
    url(r'^area/(?P<area_id>[0-9]+)/$', views.area, name='area'),
    url(r'^area/query/$', views.area_query, name='area_query'),
]
