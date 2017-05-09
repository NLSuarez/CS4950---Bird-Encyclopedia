from django.conf.urls import url

from .views import BirdList, BirdEntry

urlpatterns = [
    url(r'^$', BirdList.as_view(), name='BirdList'),
    url(r'^(?P<slug>[\w-]+)/$', BirdEntry.as_view(), name='BirdEntry'),
]
