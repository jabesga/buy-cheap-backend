from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns('',
                       url(r'^product/(?P<ean_code>\d+)/$', views.get_product, name='get_product'),
                       )