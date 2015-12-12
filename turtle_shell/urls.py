from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^animal/$', views.animal, name='person'),
    url(r'^fileupload/$', views.get_name, name='get_name'),
    url(r'^thanks/$', views.thanks, name = 'thanks'),
]