from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets,routers,serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,DjangoModelPermissions
from rest_framework.status import (HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND)
from django.views.decorators.csrf import csrf_exempt
from django_filters import FilterSet
from orders.models import Order,OrderItem
from products.models import Product
from rest_framework.renderers import JSONRenderer

# Create your views here.

class OrderSerializer(serializers.Serializer):
    firstname = serializers.CharField(max_length=150)
    lastname = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    address = serializers.CharField(max_length=160)
    city = serializers.CharField(max_length=100)
    postal_code = serializers.CharField(max_length=6)
    paid = serializers.BooleanField(default=False)

@api_view(["POST"])
def create_order(request):
    cart = request.data.get("cart")
    orderData =  request.data.get("order")
    orderData['user'] = request.user
    serializers = OrderSerializer(orderData)
    print(orderData)
   
    order = Order.objects.create(
        firstname = orderData['firstname'],
        lastname = orderData['lastname'],
        email = orderData['email'],
        address = orderData['address'],
        city = orderData['city'],
        postal_code = orderData['postal_code'],
        user = request.user
    )
    if cart:
        for item in cart:
            product = get_object_or_404(Product, id=item['id']) 
            order_item = OrderItem(
                order=order,
                product = product,
                price = item['price'],
                quantity = item['quantity']
                
            )
            order_item.save()
    else:
        order.delete()
        return Response(status=HTTP_400_BAD_REQUEST,data='Cart is Empty')
    return Response({'order_no': order.id},
                    status=HTTP_201_CREATED)

        

@api_view(["GET"])
def view_order(request):
    from django.core import serializers
    qs = Order.objects.filter(user=request.user)
    id = []
    for qs in qs:
        id.append(qs.id)
    queryset = OrderItem.objects.filter(order__in=id)
    import json
    serialized_obj = serializers.serialize('python', queryset)

    return Response(data=serialized_obj,status=HTTP_200_OK)
   