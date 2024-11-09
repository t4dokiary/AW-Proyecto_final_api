"""point_experts_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from aplicacion_dos_api.views import bootstrap
from aplicacion_dos_api.views import administrador
from aplicacion_dos_api.views import alumno
from aplicacion_dos_api.views import maestro
from aplicacion_dos_api.views import auth

urlpatterns = [
    #Version
        path('bootstrap/version', bootstrap.VersionView.as_view()),
    #Create Admin
        path('admin/', administrador.AdminView.as_view()),
    #Create Student
        path('alumno/', alumno.AlumnoView.as_view()),
    #Create Teacher
        path('maestro/', maestro.MaestroView.as_view()),
    #User Data
        path('me/', administrador.Userme.as_view()),
    #Login
        path('token/', auth.CustomAuthToken.as_view()),
    #Logout
        path('logout/', auth.Logout.as_view())
]
