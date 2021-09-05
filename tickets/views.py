from django.shortcuts import render
from django.http import JsonResponse, Http404
from rest_framework import status,filters,mixins,generics,viewsets
from rest_framework.response import Response

from .models import *
from rest_framework.decorators import api_view
from .serializers import GuestSerializer,MovieSerializer,ReservationSerializer
from rest_framework.views import APIView  ##this is for class based view.


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

#3.2 GET & PUT & DELETE
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

#CBV class based views
# 4.1 list and create == GET and POST
class CBV_list(APIView):
    def get(self,request):
        guest = Guest.objects.all()
        serializers = GuestSerializer(guest,many=True)
        return Response(serializers.data)
    def post(self,request):
        serializers = GuestSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.data,status.HTTP_400_BAD_REQUEST)

#4.2 GET & PUT & DELETE class based views --- pk
class CBV_pk(APIView):
    def get_object(self,pk):
        try:
            return Guest.objects.get(pk=pk)
        except Guest.DoesNotExists:
            raise Http404

    def get(self,request,pk):
        guest = self.get_object(pk)
        serializers = GuestSerializer(guest)
        return Response(serializers.data)

    def put(self,request,pk):
        guest = self.get_object(pk)
        serializers = GuestSerializer(guest,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        guest = self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#5.mixins
#5.1 mixins list views
class mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

#5.2 GET and PUT and DELETE
class mixins_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    def get(self,request,pk):
        return self.retrieve(request)
    def put(self,request,pk):
        return self.update(request)
    def delete(self,request,pk):
        return self.destroy(request)

#6 generics
#6.1 get & post
class generics_list(generics.ListCreateAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

#6.2 get & put & delete
class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

#7 viewsets
class viewsets_guest(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer

class viewsets_movie(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['movie']

class viewsets_reservation(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

#8 find movie
@api_view(['GET'])
def find_movie(request):
    movies = Movie.objects.filter(movie = request.data['movie'],hall = request.data['hall'])
    serializer = MovieSerializer(movies,many=True)
    return Response(serializer.data)

#9 create new reservation
@api_view(['POST'])
def create_reservation(request):
    movies= Movie.objects.get(movie = request.data['movie'],hall = request.data['hall'])
    guest = Guest()
    guest.name = request.data['name']
    guest.phone = request.data['phone']
    guest.save()
    reservation = Reservation()
    reservation.guest = guest
    reservation.movies = movies
    reservation.save()
    return Response(status=status.HTTP_201_CREATED)







