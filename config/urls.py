from django.contrib import admin
from django.conf.urls import url, include
from app.cbv.views import PublisherList

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^publishers/$', PublisherList.as_view()),
]
