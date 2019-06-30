from django.conf.urls import url, include
from rest_framework import routers
from TodoAuth.views import login,register
from django.urls import path




urlpatterns = [
    path('login/',login),
    path('register/',register)

]