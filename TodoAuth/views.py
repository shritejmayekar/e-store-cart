from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets,routers,serializers
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,DjangoModelPermissions
from rest_framework.status import (HTTP_200_OK,HTTP_201_CREATED,HTTP_400_BAD_REQUEST,HTTP_404_NOT_FOUND)
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from django.contrib.auth import authenticate


# Create your views here.

@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key,'user':user.username},
                    status=HTTP_200_OK)

@api_view(["POST"])
@permission_classes((AllowAny,))
def register(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")
    if username is None or password is None or email is None :
        return Response({'error':'Please provide username,password and email'},status=HTTP_400_BAD_REQUEST)
    if User.objects.filter(username=username).count() > 0:
        return Response({'error':'username already taken'},status=HTTP_400_BAD_REQUEST)
    user = User.objects.create_user(username=username,password=password,email=email)

    return Response({'Success':'Register sucess {}'.format(user)},status=HTTP_201_CREATED)





