"""
URL configuration for portflyCrab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import index , main , login ,loginv , validator, register, register_user 
from .views import portindex,main
from .views import about , transformpdf
from django.urls import path
from . import views
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.main, name='main'),
    path('loginv/', views.loginv, name='loginv'),
    path('logout/', views.logout_view, name='logout'),
    path('loginv/portindex/', views.portindex, name='loginv_portindex_redirect'),
    path('login', views.login_view, name='login_view'),
    path('portindex/', views.portindex, name='portindex'),
    path('register_user/', views.register_user, name='register_user'),
    path('validator/', views.validator, name='validator'),
    path('register/', views.register, name='register'),
    path('about/', about, name='about'),
    path('transformpdf/', transformpdf, name='transformpdf'),
]
