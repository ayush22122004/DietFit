"""
URL configuration for backend project.

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
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/',views.login),
    path('api/signup/',views.signup),
    path('api/diet-plan/',views.chat),
    path('api/get-csrf-token/',views.csrf_exempt),
    path('buy/', views.buy_product),
    path('api/chatbox/', views.chatbox),
    path('api/del/',views.del_data),
    path('api/get-meal-by-cal/', views.get_meal_by_cal),
    path('api/get-meal-by-ingredient/', views.get_meal_by_ingredient),
]