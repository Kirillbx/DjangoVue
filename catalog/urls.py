from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^product/$', APIProduct.as_view(), name='product-list'),
    url(r'^product/create/$', APIProductCreate.as_view(), name='product-create'),
    url(r'^product/(?P<id>\d+)/$', APIProduct.as_view(), name='product-detail'),
    url(r'^productcategories/$', APIProductCategories.as_view(), name='prodcat-list'),
    url(r'^productcategories/create/$', APIProductCategoriesCreate.as_view(), name='productcategories-create'),
    url(r'^productcategories/(?P<id>\d+)/$', APIProductCategories.as_view(), name='prodcat-detail'),
]