# from django.conf.urls import url
# from products.views import ProductViewSet

# urlpatterns = [
#     url(r'^$',ProductViewSet, name='product_list'),
#     # url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
#     # url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
# ]
from django.urls import path,include
from django.conf.urls import url
from products.views import ProductViewSet,CategoryViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'product',ProductViewSet)
router.register(r'category',CategoryViewSet)

urlpatterns = [
    path(r'',include(router.urls))
]