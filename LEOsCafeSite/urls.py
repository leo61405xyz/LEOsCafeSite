"""
URL configuration for LEOsCafeSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from LEOsCafeSiteapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
	path('', views.index),
	path('index/', views.index),
    path('ordercafe/', views.ordercafe),
    path('orderview/', views.orderview),
    path('login/', views.login),
    path('logout/', views.logout),
    path('adminmain/', views.adminmain),
    path('cafeedit/<int:cafeid>/', views.cafeedit),
    path('cafeedit/<int:cafeid>/<str:mode>/', views.cafeedit),
    path('cafedelete/<int:cafeid>/', views.cafedelete),
    path('cafeadd/', views.cafeadd),
    path('orderdelete/<int:orderid>/', views.orderdelete),
    path('orderedit/<int:orderid>/', views.orderedit),
    path('orderedit/<int:orderid>/<str:mode>/', views.orderedit),
    path('captcha/', include('captcha.urls')),
]
