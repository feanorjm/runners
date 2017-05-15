"""runners URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from main.views import carrera_crear, corredor_crear, categoria_crear, distancia_crear, getCateCarrera, getDisCarrera,iniciar_carrera, getDataCorredor,setTimeInicio

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', carrera_crear, name="carrera_crear"),
    url(r'^carreras/$', carrera_crear, name="carrera_crear"),
    url(r'^corredor/$', corredor_crear, name="corredor_crear"),
    url(r'^categorias/$', categoria_crear, name="categoria_crear"),
    url(r'^distancias/$', distancia_crear, name="distancia_crear"),
    url(r'^getCateCarrera/$', getCateCarrera, name="getCateCarrera"),
    url(r'^getDisCarrera/$', getDisCarrera, name="getDisCarrera"),
    url(r'^iniciar_carrera/$', iniciar_carrera, name="iniciar_carrera"),
    url(r'^getDataCorredor/$', getDataCorredor, name="getDataCorredor"),
    url(r'^setTimeInicio/$', setTimeInicio, name="setTimeInicio"),
]
