from django.shortcuts import render
from rest_framework import viewsets,routers,serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,DjangoModelPermissions
from rest_framework.status import (HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND)
from django.views.decorators.csrf import csrf_exempt
from products.models import Product,Category
from products.serializers import ProductSerializer,CategorySerializer
from django_filters import FilterSet
# Create your views here.

@permission_classes((AllowAny,))
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get']
    def list(self, request, *args, **kwargs):
        category = request.query_params.get('category')
        if category:
            queryset = self.filter_queryset(self.get_queryset()).filter(category__slug=category)
        else:
            queryset = self.filter_queryset(self.get_queryset()).filter(available=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
        


@permission_classes((AllowAny,))
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get']
    