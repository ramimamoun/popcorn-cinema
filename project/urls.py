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
    path('rest/fb/<int:pk>',views.FBV_pk),
]
