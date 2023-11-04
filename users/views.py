from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView

from . models import User
from . serializers import registerUserSerializer

# Create your views here.
@api_view(['POST'])
def register(request):
  data=request.data
  user=User.objects.create(
    username=data['username'],
    email=data['email'],
    names=data['names'],
    last_names=data['last_names'],
    password=make_password(data['password'])
  )
  serializer=registerUserSerializer(user,many=False)
  return Response(serializer.data)