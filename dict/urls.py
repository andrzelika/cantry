from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^(?P<ask>[0-9]{4})/$', views.definition_view, name='definition_view'),
]
