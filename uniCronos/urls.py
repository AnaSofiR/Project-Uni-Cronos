"""
URL configuration for uniCronos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from uniweb import views as uniCronosViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', uniCronosViews.inicio, name='inicio'),
    path('principal/', uniCronosViews.principal, name='principal'),
    path('buscar/<str:lista>/',uniCronosViews.buscar, name='buscar'),
    path('horario/<str:horario1>/<str:horario2>/<str:horario3>/', uniCronosViews.horario, name='horario'),
    path('sugerencias/', uniCronosViews.sugerencias, name='sugerencias'),
]


