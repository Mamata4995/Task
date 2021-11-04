from django.conf.urls import url
from product import views


urlpatterns = [
    url(r'^$',views.ProductView.as_view(),name='product_basic'),
    url(r'^$',views.ProductListView.as_view(), name='product_list'),
    url(r'^product/(?P<pk>\d+)$',views.ProductDetailView.as_view(), name='product_detail'),
    url(r'^product/new/$',views.ProductCreateView.as_view(),name='product_new'),
    url(r'^product/(?P<pk>\d+)/edit/$',views.ProductUpdateView.as_view(),name='product_edit'),
    url(r'^product/(?P<pk>\d+)/remove/$',views.ProductDeleteView.as_view(),name='product_remove'),
    url(r'^drafts/$',views.DraftListView.as_view(),name='product_draft_list'),
    url(r'^product/(?P<pk>\d+)/publish/$',views.product_publish,name='product_publish'),
]
