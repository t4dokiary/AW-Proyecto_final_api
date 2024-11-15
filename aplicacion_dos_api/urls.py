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
from aplicacion_dos_api.views import users
from aplicacion_dos_api.views import alumno
from aplicacion_dos_api.views import maestro
from aplicacion_dos_api.views import auth

urlpatterns = [
    #versiones
        path('bootstrap/version', bootstrap.VersionView.as_view()),
    
    #Administradores
    #Crear
        path('admin/', users.AdminView.as_view()),
    #Listar
        path('lista-admins/', users.AdminAll.as_view()),
    #Editar
        path('admins-edit/', users.AdminsViewEdit.as_view()),
        
    #Alumnos
    #Crear
        path('alumnos/', alumno.AlumnoView.as_view()),
    #Listar
        path('lista-alumnos/', alumno.AlumnoAll.as_view()),
    #Editar
        path('alumnos-edit/', alumno.AlumnosViewEdit.as_view()),
    
    #Maestros
    #Crear
        path('maestro/', maestro.MaestrosView.as_view()),
    #Listar
        path('lista-maestros/', maestro.MaestrosAll.as_view()),
    #Editar
        path('maestros-edit/', maestro.MaestrosViewEdit.as_view()),
        
    #Servicios de autenticacion
    #Login
        path('token/', auth.CustomAuthToken.as_view()),
    #Logout
        path('logout/', auth.Logout.as_view())
]
