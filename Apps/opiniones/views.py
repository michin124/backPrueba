from django.shortcuts import render

# Create your views here.

from django.db.models import Avg

from django.http import HttpResponse

from django.shortcuts import render
# Create your views here.
from math import *
import math
from email import message
from unicodedata import name
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from ..user.models import User
from ..libro.models import libro
from .models import Opinion
import json


class opinionview(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0):

        if(id!=''):      
            users=list(Opinion.objects.filter(idLibro=id).values())
            if len(users)>0:
                    datos={'message':"succes",'Opiniones':list(reversed(users))}
            else:
                    datos={'message':"producto no encontradas"}  
            return JsonResponse(datos)

        else:
            Opiniones=list(Opinion.objects.values())
            if len(Opiniones)>0:
                datos={'Opiniones':Opiniones}
            else:
                datos={'message':"no se encuentran producto"}
            return JsonResponse(datos)

    def post(self,request):

        print(request.body)
        jd=json.loads(request.body)
        Opinion.objects.create(nombreUser=jd['nombreU'],calificacion=jd['calificacion'],descripcion=jd['descripcion'],idUser=User.objects.get(id=jd['idU']),idLibro=libro.objects.get(id=jd['idL']),date=jd['date'])
        Estrellas = Opinion.objects.filter(idLibro=jd['idL']).aggregate(promedio=Avg('calificacion'))
        libreria = list(libro.objects.filter(id=jd['idL']).values())
        if len(libreria)>0:
            libros=libro.objects.get(id=jd['idL'])
            libros.calificacion=Estrellas['promedio']
            libros.save()

        datos={'message':'succes'}
        return JsonResponse(datos)


