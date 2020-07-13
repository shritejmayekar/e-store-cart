# from django.conf.urls import url
# from products.views import ProductViewSet

# urlpatterns = [
#     url(r'^$',ProductViewSet, name='product_list'),
#     # url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
#     # url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
# ]
from django.urls import path,include
from django.conf.urls import url
from orders.views import create_order,view_order,view_order_v2

urlpatterns = [
    path('create/',create_order),
    path('view/',view_order),
    path('view_v2/',view_order_v2)
]
