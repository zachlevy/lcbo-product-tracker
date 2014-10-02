from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from producttracker import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^update-product/(?P<product_id>.*)$', views.update_product, name="update_product"),
	url(r'^bigboard/product/(?P<product_id>.*)$', views.product, name="product"),
	url(r'^update-inventory/(?P<product_id>.*)$', views.update_inventory, name="update_inventory"),
	url(r'^admin/', include(admin.site.urls)),
)