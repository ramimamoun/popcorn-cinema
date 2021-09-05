"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from tickets import views
from django.urls import path,include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guest',views.viewsets_guest)
router.register('movie',views.viewsets_movie)
router.register('reservation',views.viewsets_reservation)

urlpatterns = [
    path('rami/', admin.site.urls),
    # path('', include('tickets.urls',namespace='tickets')),
    #1
    path('django/jasonresponsenomodel/',views.no_rest_no_model),
    #2
    path('django/',views.no_rest_from_model),
    #3.1 GET & POST from rest freamework function based view @api_view
    path('rest/fbv/',views.FBV_list),
    #3.2 GET & PUT & DELETE from rest freamework function based view @api_view
    path('rest/fbv/<int:pk>',views.FBV_pk),
    #4.1 GET & POST  from rest freamework class based view APIView
    path('rest/cbv/',views.CBV_list.as_view()),
    #4.2 GET & PUT & DELETE from rest freamework class based view APIView
    path('rest/cbv/<int:pk>',views.CBV_pk.as_view()),
    #5.1 GET & POST  from rest freamework class mixins
    path('rest/mbv/',views.mixins_list.as_view()),
    #4.2 GET & PUT & DELETE from rest freamework class mixins pk
    path('rest/mbv/<int:pk>',views.mixins_pk.as_view()),
    #6.1 GET & POST  from rest freamework class gemerics
    path('rest/gbv/',views.generics_list.as_view()),
    #6.2 GET & PUT & DELETE from rest freamework class gemerics pk
    path('rest/gbv/<int:pk>',views.generics_pk.as_view()),
    #7 viewsets
    path('rest/v/',include(router.urls)),
    #8 find movie
    path('rest/ffbv/',views.find_movie),
    #9 create reservation
    path('rest/res/',views.create_reservation),








]
