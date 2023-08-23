from django.shortcuts import render

# Create your views here.

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
from .models import User
from ..preguntaS.models import Pregunta
import json

#from django.http import HttpResponse

# Create your views here.
#def home(request):
#   return HttpResponse("<h1>hi</h1>")
    #listatiendas=Tienda.objects.all()
    #return render(request,"gestions.html",{"Tiendas":listatiendas})

class userview(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=0,correo='',password='',email='',idP=0):
        
        if(idP>0):      
            
            pregunta=list(Pregunta.objects.filter(id=idP).values())
            if len(pregunta)>0:
                    datos={'message':"succes",'Opiniones':pregunta}
            else:
                    datos={'message':"producto no encontradas"}  
            return JsonResponse(datos)

        if(correo!=''):      
            users=list(User.objects.filter(Correo=correo,Password=password).values())
            if len(users)>0:
                    datos={'message':"succes",'Opiniones':users}
            else:
                    datos={'message':"producto no encontradas"}  
            return JsonResponse(datos)

        if(email!=''):      
            users=list(User.objects.filter(Correo=email).values())
            if len(users)>0:
                    datos={'message':"succes",'Opiniones':users}
            else:
                    datos={'message':"producto no encontradas"}  
            return JsonResponse(datos)

        if(id>0):      
            users=list(User.objects.filter(id=id).values())
            if len(users)>0:
                    datos={'message':"succes",'Opiniones':users}
            else:
                    datos={'message':"producto no encontradas"}  
            return JsonResponse(datos)

        else:
            Opiniones=list(User.objects.values())
            if len(Opiniones)>0:
                datos={'Opiniones':Opiniones}
            else:
                datos={'message':"no se encuentran producto"}
            return JsonResponse(datos)

    def post(self,request,valid=''):

        print(request.body)
        jd=json.loads(request.body)
        if(valid==''):
            User.objects.create(Nombre=jd['Nombre'],Correo=jd['Correo'],Password=jd['Password'],Answer=jd['Answer'],IdRespuesta=Pregunta.objects.get(id=jd['Pregunta']))
            datos={'message':'succes'}
            return JsonResponse(datos)
        if(valid=='uno'):
            users=list(User.objects.filter(Correo=jd['correo'],Password=jd['contrasena']).values())
            datos={'message':'succes','Opiniones':users}
            return JsonResponse(datos)
        
    
    def put(self,request, id):
        jd=json.loads(request.body)
        Users=list(User.objects.filter(id=id,Answer=jd['respuesta']).values())
        if len(Users)>0:
            usr=User.objects.get(id=id,Answer=jd['respuesta'])
            usr.Password=jd['confirmContra']
            
            usr.save()
            datos={'message':"ya tiendas"}
        else:
            datos={'message':"no se encuentran tiendas"}
        return JsonResponse(datos)