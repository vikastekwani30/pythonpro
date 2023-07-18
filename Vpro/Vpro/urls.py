"""Vpro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from Vapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    # path('imgdemo/',views.showImg),
    # path('ahmedabad/',views.ahmedabad),
    # path('gandhinagar/',views.gandhinagar),
    # path('rajkot/',views.rajkot),
    # path('surat/',views.surat),
    path('india/',views.india),
    path('argentina/',views.argentina),
    path('uk/',views.uk),
    path('usa/',views.usa),
    path('russia/',views.russia),
    path('germany/',views.germany),
    path('brazil/',views.brazil),
]
