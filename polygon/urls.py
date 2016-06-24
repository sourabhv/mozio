from django.conf.urls import include, url

from . import views

urlpatterns = [
    url(r'^provider/$', views.provider_list),
    url(r'^provider/(?P<provider_id>[0-9]+)/$', views.provider_detail),
    url(r'^provider/(?P<provider_id>[0-9]+)/area/$', views.provider_area_list),
    url(r'^provider/(?P<provider_id>[0-9]+)/area/(?P<area_id>[0-9]+)/$', views.provider_area_detail),
    url(r'^provider/(?P<provider_id>[0-9]+)/area/query/$', views.provider_area_query),

    url(r'^area/$', views.area_list),
    url(r'^area/(?P<area_id>[0-9]+)/$', views.area_detail),
    url(r'^area/query/$', views.area_query),
]
