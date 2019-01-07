"""Server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URTEML to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rest_framework.authtoken import views

from Station_controls.views import home, SendView, view_data_available, request_data, view_stations_available

urlpatterns = [
    path('home/', home, name='home'),
    path('send/', SendView.send, name='send'),
    path('obtain_token/', views.obtain_auth_token),
    path('view_data_available/', view_data_available, name='view_data_available'),
    path('request_data/', request_data, name='request_data'),
    path('view_stations_available/', view_stations_available, name='view_stations_available')
]
