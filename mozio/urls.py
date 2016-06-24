from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^api/', include('polygon.urls', namespace='polygon')),
    url(r'^admin/', admin.site.urls),
]
