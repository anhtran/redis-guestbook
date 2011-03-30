from django.conf.urls.defaults import *


urlpatterns = patterns('notebook.views',
    url(r'^$', 'index', name='index-page'),
    url(r'^ajax/request/send/$', 'ajax_save', name='send-request'),
)
