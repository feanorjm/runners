from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
import simplejson
from django.core import serializers
from main.forms import CarreraForm, CorredorForm, CategoriaForm, DistanciaForm
from main.models import Carrera, Categoria, Distancia, Corredor, Posicion
import json
from django.views.decorators.csrf import csrf_protect
from django.db.models import Max
import time
from datetime import datetime


def carrera_crear(request):
    mensaje = "None"

    if request.method == 'POST':
        form = CarreraForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
            mensaje = "Carrera Ingresada Correctamente"
        else:
            mensaje = "Carrera No Ingresada. Datos Incorrectos"
    else:
        form = CarreraForm()
    carreras = Carrera.objects.all().only('id', 'nombre')

    return render(request, 'carreras.html',{'mensaje': mensaje,'form': form,'carreras':carreras})

def corredor_crear(request):
    mensaje = "None"
    if request.method == 'POST':
        form = CorredorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
            mensaje = "Corredor Ingresado Correctamente"
        else:
            mensaje = "Corredor No Ingresado. Datos Incorrectos"
    else:
        form = CorredorForm()
    return render(request, 'corredor.html',{'mensaje': mensaje,'form': form})

def categoria_crear(request):
    mensaje = "None"
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
            mensaje = "Categoría Ingresada Correctamente"
        else:
            mensaje = "Categoría No Ingresada. Datos Incorrectos"
    else:
        form = CategoriaForm()

    cate = Categoria.objects.all().only('id', 'nombre', 'edad_ini', 'edad_fin', 'sexo').order_by('-id')[:10]

    print(mensaje)
    return render(request, 'categorias.html',{'mensaje': mensaje,'form': form, 'categorias':cate})

def distancia_crear(request):
    mensaje = "None"
    if request.method == 'POST':
        form = DistanciaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
            mensaje = "Distancia Ingresada Correctamente"
        else:
            mensaje = "Distancia No Ingresada. Datos Incorrectos"
    else:
        form = DistanciaForm()

    dis = Distancia.objects.all().only('id', 'nombre', 'distancia').order_by('-id')[:10]
    return render(request, 'distancias.html',{'mensaje': mensaje,'form': form, 'distancias':dis})

def getCateCarrera(request):
    '''JSONdata = request.POST['id']
    dict = simplejson.JSONDecoder().decode(JSONdata)
    id = dict['id']'''
    id = request.POST['id']
    cate = Categoria.objects.all().only('id', 'nombre','edad_ini','edad_fin','sexo').filter(carrera=id)
    # data = {'baz': 'goo', 'foo': 'bar'}
    # json_data = simplejson.dumps(carreras)
    cate_json = serializers.serialize("json", cate, fields=('id', 'nombre','edad_ini','edad_fin','sexo'))

    return HttpResponse(cate_json, content_type="application/json")

def getDisCarrera(request):
    id = request.POST['id']
    dis = Distancia.objects.all().only('id', 'nombre','distancia').filter(carrera=id)
    dis_json = serializers.serialize("json", dis, fields=('id', 'nombre','distancia'))

    return HttpResponse(dis_json, content_type="application/json")

def getDataCorredor(request):
    numero_post = request.POST['numero']
    #obtener datos, id_categoría e id_distancia
    cont = Posicion.objects.filter(numero=numero_post).count()
    if cont == 0:
        data_corre = Corredor.objects.only('id', 'categoria', 'categoria__nombre','distancia','distancia__nombre','team').filter(numero=numero_post)
        if (data_corre.count() > 0):
            data_v = data_corre.values('id', 'nombre','apellido_pat', 'categoria', 'categoria__nombre','distancia','distancia__nombre', 'team')[0]
            #corre_json = serializers.serialize("json", data_v, fields=('id', 'categoria', 'categoria__nombre','distancia','distancia__nombre'))
            dis = data_corre.values()[0]['distancia_id']
            cat = data_corre.values()[0]['categoria_id']
            id_c = data_corre.values()[0]['id']
            team_c = data_corre.values()[0]['team']
            posicion = Posicion.objects.filter(categoria_id=cat,distancia_id=dis).aggregate(Max('lugar_cat_dis'))['lugar_cat_dis__max']
            pos = 0
            if posicion is not None:
                pos = int(posicion) + 1
                data_v['posicion'] = pos
            else:
                pos = 1
                data_v['posicion'] = pos

            pos_gen = Posicion.objects.filter(distancia_id=dis).aggregate(Max('lugar_gen'))['lugar_gen__max']
            posi_gen = 0
            if pos_gen is not None:
                posi_gen = int(pos_gen) + 1
                data_v['posicion_gen'] = posi_gen
            else:
                posi_gen = 1
                data_v['posicion_gen'] = posi_gen

            hora_llegada = time.strftime("%H:%M:%S")
            hora_distancia_ini = Distancia.objects.values('hora_inicio').filter(pk=dis)[0]['hora_inicio']
            FMT = '%H:%M:%S'
            tdelta = datetime.strptime(str(hora_llegada), FMT) - datetime.strptime(str(hora_distancia_ini), FMT)
            data_v['tiempo'] = str(tdelta)

            p_final = Posicion(numero=numero_post, tiempo=str(tdelta), id_corredor=id_c,categoria_id=cat,distancia_id=dis,team=team_c,lugar_cat_dis=pos,lugar_gen=posi_gen)
            p_final.save()


            json_data = simplejson.dumps(data_v)
        else:
            json_data = simplejson.dumps({'estado':0})
    else:
        json_data = simplejson.dumps({'estado': 0})

    return HttpResponse(json_data, content_type="application/json")

def iniciar_carrera(request):
    id_carrera = request.POST.get('sel_carre')
    dis = Distancia.objects.all().only('id').filter(carrera=id_carrera)
    cat = Categoria.objects.all().only('id').filter(carrera=id_carrera)

    return render(request, 'iniciar_carrera.html',{'distancias':dis,'categorias':cat})

def setTimeInicio(request):
    id_dis = request.POST['id_dis']
    hora = time.strftime("%H:%M:%S")
    Distancia.objects.filter(pk=id_dis).update(hora_inicio=hora)
    json_data = simplejson.dumps({'hola':'hola'})

    return HttpResponse(json_data, content_type="application/json")
