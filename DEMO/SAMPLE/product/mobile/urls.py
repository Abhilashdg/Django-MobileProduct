from django.conf.urls import url
from . import views
urlpatterns = [
 # cuisine_list view as a class
 url(r'^$', views.ProductListView.as_view(), name='mobile_list_cls'),
 # Cuisine_list view as a function
 # url(r'^$', views.Cuisine_list, name='Cuisine_list' ),
 # Cuisine_detail view as a function
 url(r'^(?P<mobile>[-\w]+)/$',

 views.Product_detail,
 name='Product_detail'
 ),
]
