from django.conf.urls import url

from . import views

app_name = 'myapp'
urlpatterns = [

    #ProjectONE
    url(r'^index/$', views.index),
    url(r'^home/$', views.home),
    url(r'^dataset/$', views.dataset),
    url(r'^regressions/$', views.regressions),
    url(r'^graphs/$', views.graphs),
    #url(r'^display_table/$', views.display_table, name='display_table'),

]
