from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import status,filters
from rest_framework.response import Response

from .models import *
from rest_framework.decorators import api_view
from .serializers import GuestSerializer,MovieSerializer,ReservationSerializer

# Create your views here.

# 1. without Rest framework & no model query FBV.
def no_rest_no_model(request):
    guest = [
        {
            'id': 1,
            'name': 'omer',
            'phone': 123456788765,
        },
        {
            'id': 2,
            'name': 'omer',
            'phone': 123456788765,
        }
    ]
    return JsonResponse(guest,safe=False)

# 2 model data default django without rest.
def no_rest_from_model(request):
    data = Guest.objects.all()
    response = {
        'guest':list(data.values('name','phone'))
    }
    return JsonResponse(response)

#List == GET
#Create == POST
#Update == PUT
#PK query == GET
#delete == DElETE
##3 Function based views:

#3.1 GET & POST
@api_view(['GET','POST']) ##his name is decorators
def FBV_list(request): ##functions based views

    #GET
    if request.method =='GET':
        guests = Guest.objects.all()
        serializer = GuestSerializer(guests,many=True)
        return Response(serializer.data)
    #POST
    elif request.method == 'POST':
        serializer = GuestSerializer(data=request.data) ##update date
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data,status.HTTP_400_BAD_REQUEST)

#3.1 GET & PUT & DELETE
@api_view(['GET','PUT','DELETE'])
def FBV_pk(request,pk): #he can choice by pk only
    try:
        guest = Guest.objects.get(pk=pk)
    except Guest.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #GET
    if request.method =='GET':
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    #PUT
    elif request.method == 'PUT':
        serializer = GuestSerializer(guest,data=request.data) #add guest
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status.HTTP_200_OK)
        return Response(serializer.errors,status.HTTP_400_BAD_REQUEST)
    #DELETE
    elif request.method =='DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)