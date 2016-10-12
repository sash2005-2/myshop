from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index_tmpl'),
    url(r'^list/$', views.product_list, name='product_list'),
    url(r'^base/$', views.base, name='base_tmpl'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
