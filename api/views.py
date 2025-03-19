from multiprocessing.managers import BaseManager
from django.shortcuts import render
from rest_framework import generics 
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from django.core.serializers.json import DjangoJSONEncoder  
from django.http import JsonResponse
from decimal import Decimal

from .serializers import ClienteSerializer, GastoConductorSerializer
from elim.models import Cliente, GastoConductor, PerfilConductor

import json

class ClienteList(APIView):
    def get(self,request):    
        return Response(ClienteSerializer(Cliente.objects.all(),many=True).data)


def gastoConductorListReloadAux(request):    
    draw = (request.GET.get('draw'))
    start = (request.GET.get('start'))
    length = (request.GET.get('length'))
    search = str(request.GET.get('search[value]'))
    
    # if search.__len__() > 3 and search.lower().__contains__('acep'):
    #     search = search.replace('acep','1')
    # elif search.__len__() > 3 and search.lower().__contains__('rech'):
    #     search = search.replace('rech','0')
    # if search:
    queryset:BaseManager[GastoConductor] = GastoConductor.objects.filter(                
                # (
                # Q(concepto__icontains=search)|
                # Q(estado_aceptacion__icontains=search)|
                # Q(medio_pago__icontains=search)|
                # Q(descripcion__icontains=search)|
                # Q(factura__icontains=search)|
                # Q(valor__icontains=search)
                # ),
                estado = True ).order_by('-id')

    if request.user.is_superuser:            
        queryset = queryset #[start:start+length]
    elif perfil := PerfilConductor.objects.filter(usuario = request.user).first():
        queryset = queryset.filter(vehiculo = perfil.vehiculo) #[start:start+length]
    page_number = 1
    # page_number = int((start+length)/10)
    paginator = Paginator(queryset,10)
    try:
        # if draw > paginator.num_pages:
        #     draw -= paginator.num_pages 
        obj = paginator.get_page(page_number).object_list        
    except PageNotAnInteger:
        obj = paginator.get_page(page_number).object_list
    except EmptyPage:
        obj = paginator.get_page(paginator.num_pages).object_list
    
    datos = [
        {
            "id": d.id,
            "fecha": d.fecha,
            "estado_aceptacion":d.estado_aceptacion,
            "concepto": d.concepto,
            "medio_pago": d.medio_pago,
            "factura": str(d.factura),
            "valor": d.valor,
            "efectivo":d.efectivo,
            "credito":d.credito,
            "transferencia":d.transferencia,
            "descripcion": d.descripcion,
        } for d in obj
    ]
    context = {
        'data':list(GastoConductor.objects.values()),
        'draw':draw,         
        'recordsTotal': queryset.count(),
        'recordsFiltered':queryset.count()
    }
    return JsonResponse(context, safe=False)


def gastoConductorListReload(request):        
    queryset:BaseManager[GastoConductor] = GastoConductor.objects.filter(estado=True).order_by('-id')
    if request.user.is_superuser:            
        queryset = queryset
    elif perfil := PerfilConductor.objects.filter(usuario = request.user).first():
        queryset = queryset.filter(vehiculo = perfil.vehiculo)        
    def s_color(valor):
        if(valor<10000):
            return 'red'
        elif(valor>=10000 and valor<20000):
            return 'orange'
        elif(valor>=20000 and valor<40000):
            return 'blue'
        elif(valor>=100000 and valor<500000):
            return 'green'
        elif(valor>=500000):
            return 'yellow'    
    datos = [
        {
            "id": d.id,
            "fecha": d.fecha,
            "estado_aceptacion":d.estado_aceptacion,
            "concepto": d.concepto,
            "medio_pago": d.medio_pago,
            "factura": str(d.factura),
            "color": s_color(d.valor),
            "valor": d.valor,
            "efectivo":d.efectivo,
            "credito":d.credito,
            "transferencia":d.transferencia,
            "descripcion": d.descripcion,
        } for d in queryset
    ]
    context = {'data':datos}
    return JsonResponse(context)

class GastoConductorList(generics.ListAPIView):
    queryset = GastoConductor.objects.filter(estado=True).order_by('-id')
    serializer_class = GastoConductorSerializer
    
    
    def get_queryset(self):        
        
        # context = super(GastoConductor).get_context_data(**kwargs)
        
        draw = int(self.request.GET.get('draw'))
        start = int(self.request.GET.get('start'))
        length = int(self.request.GET.get('length'))
        search = str(self.request.GET.get('search[value]'))
        order = self.request.GET.get('order[0][dir]')
        order_num_col = self.request.GET.get('order[0][column]')
        
        if search.__len__() > 3 and search.lower().__contains__('acep'):
            search = search.replace('acep','1')            
        elif search.__len__() > 3 and search.lower().__contains__('rech'):
            search = search.replace('rech','0')
        
        aux = { '3':'estado_aceptacion','4':'concepto',
                '5':'medio_pago','6':'factura','7':"valor",
                '8':"efectivo",'9':"credito",'10':"transferencia",'11':"descripcion"}
        queryset:BaseManager[GastoConductor] = GastoConductor.objects.filter(                
                    (Q(concepto__icontains=search)|
                    Q(estado_aceptacion__icontains=search)|
                    Q(medio_pago__icontains=search)|
                    Q(descripcion__icontains=search)|
                    Q(factura__icontains=search)|
                    Q(valor__icontains=search)),
                    estado = True ).order_by('-id')

        if order_num_col is not None and order is not None and order_num_col in aux:
            ree = aux[order_num_col]
            if order == 'asc':                
                queryset = queryset.order_by(ree)
            else:
                queryset = queryset.order_by(f'-{ree}')

        if self.request.user.is_superuser:            
            return queryset[start:start+length]
        elif perfil:=PerfilConductor.objects.filter(usuario = self.request.user).first():
            return queryset.filter(vehiculo = perfil.vehiculo)[start:start+length]
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        draw = int(self.request.GET.get('draw'))
        context['draw'] = draw        
        context['recordsTotal'] = int(self.queryset.count())
        context['recordsFiltered'] = int(self.queryset.count())        
        
        # queryset = self.filter_queryset(self.get_queryset())
        paginator = Paginator(self.queryset,10)
        try:
            obj = paginator.page(draw).object_list
        except PageNotAnInteger:
            obj = paginator.page(draw).object_list
        except EmptyPage:
            obj = paginator.page(paginator.num_pages).object_list
        
        datos = [
            {
                "id":d.id ,
                "fecha":d.fecha,
                "estado_aceptacion":d.estado_aceptacion,
                "concepto": d.concepto,
                "medio_pago": d.medio_pago,
                "factura": d.factura,
                "valor": d.valor,
                "efectivo": d.efectivo,
                "credito": d.credito,
                "transferencia": d.transferencia,
                "descripcion": d.descripcion,
            } for d in obj
        ]
        # context ['obj'] = datos
        return context
