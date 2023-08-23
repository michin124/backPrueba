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
from .models import Categoria

#from django.http import HttpResponse

# Create your views here.
#def home(request):
#   return HttpResponse("<h1>hi</h1>")
    #listatiendas=Tienda.objects.all()
    #return render(request,"gestions.html",{"Tiendas":listatiendas})

class categoriaview(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)
    def get(self,request,id=0,categoria=0):
    
        if(id>0):
                
            Cat=list(Categoria.objects.filter(id=id).values())
            if len(Cat)>0:
                    datos={'message':"succes",'Categoria':Cat}
            else:
                    datos={'message':"producto no encontradas"}  
            return JsonResponse(datos) 
        
        else:
            Cat=list(Categoria.objects.values())
            if len(Cat)>0:
                    datos={'message':"succes",'Categoria':Cat}
            else:
                    datos={'message':"producto no encontradas"}  
            return JsonResponse(datos)