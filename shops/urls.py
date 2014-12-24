from django.conf.urls import patterns, url, include

from shops import views

urlpatterns = patterns('',
   # ex: /polls/
    url(r'^/new/$', views.new, name='new'),
    url(r'^/create/$', views.create, name='create'),
    url(r'^/all_shops/$', views.all_shops, name='all_shops'),
    url(r'^/new_product/$', views.new_product, name='new_product'),
    url(r'^/create_product/$', views.create_product, name='create_product'),
    url(r'^/all_products/$', views.all_products, name='all_products'),
    url(r'^/new_item/$', views.new_item, name='new_item'),
    url(r'^/create_item/$', views.create_item, name='create_item'),
    url(r'^/all_items/$', views.all_items, name='all_items'),
    url(r'^/(?P<item_id>\d+)/$', views.item_detail, name='item_detail'),
    url(r'^/payment/(?P<item_id>\d+)/$', views.create_payment_stripe, name='create_payment_stripe'),
    url(r'^/payment_model/(?P<item_id>\d+)/$', views.payment_model, name='payment_model'),
    url(r'^/delete_item/(?P<item_id>\d+)/$', views.delete_item, name='delete_item'),
    url(r'^/edit_item/(?P<item_id>\d+)/$', views.edit_item, name='edit_item'),
    url(r'^/update_item/$', views.update_item, name='update_item'),



)