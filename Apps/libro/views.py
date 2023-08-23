from django.shortcuts import render
import difflib
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
from .models import libro
from ..categorias.models import Categoria

#from django.http import HttpResponse

# Create your views here.
#def home(request):
#   return HttpResponse("<h1>hi</h1>")
    #listalibros=libro.objects.all()
    #return render(request,"gestions.html",{"libros":listalibros})

class libroview(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs) :
        return super().dispatch(request, *args, **kwargs)
    def get(self,request,id=0,categoria=0,search=''):

        if(search!=''):
            libros6=list(libro.objects.filter().values())
            categorias=list(Categoria.objects.filter().values())

            valor = search.lower() 
            palabras_search = valor.split() 

            libros_similares6 = []
            autores_similares6 = []
            cate_similares6 = []
            for libro6 in libros6:
                nombre_libro = libro6['nombre'].lower()
                palabras_libro = nombre_libro.split()
                if all(difflib.get_close_matches(palabra, palabras_libro, n=1, cutoff=0.7) for palabra in palabras_search):
                    libros_similares6.append(libro6)

                autor_libro = libro6['Autor'].lower()
                autores_libro = autor_libro.split()  
                if all(difflib.get_close_matches(palabra, autores_libro, n=1, cutoff=0.7) for palabra in palabras_search):
                    autores_similares6.append(libro6)
            for categorias in categorias:
                cate_libro = categorias['tipocategoria'].lower()
                cates_libro = cate_libro.split()  
                if all(difflib.get_close_matches(palabra, cates_libro, n=1, cutoff=0.7) for palabra in palabras_search):
                    cate_similares6.append(categorias)


            if len(libros_similares6)>0:
                    datos={'message':"succeso",'libros':libros_similares6}
            else:
                    datos={'message':"libros no encontradas"}
            if len(autores_similares6)>0:
                    datos2={'message':"succeso",'libros':autores_similares6}
            else:
                    datos2={'message':"libros no encontradas"}
            if len(cate_similares6)>0:
                    datos3={'message':"succeso",'categorias':cate_similares6}
            else:
                    datos3={'message':"libros no encontradas"}
                
            datosF={'message':"succeso",'libros':datos,'autores':datos2,'categorias':datos3}
            return JsonResponse(datosF)
    
        if(id>0):
                
            book=list(libro.objects.filter(id=id).values())
            cat = list(Categoria.objects.filter().values())
            if len(book)>0:
                    datos={'message':"succes",'book':book,'categoria':cat[book[0]['categoria_id']]['tipocategoria']}
            else:
                    datos={'message':"producto no encontradas"}  
            return JsonResponse(datos) 
        
        
        
        if(categoria>0):
                book=list(libro.objects.filter(categoria=categoria).values())
                if len(book)>0:
                        datos={'message':"succes",'book':book}
                else:
                        datos={'message':"producto no encontradas"}  
                return JsonResponse(datos) 
        

        
        else:
            book=list(libro.objects.values())
            if len(book)>0:
                    datos={'message':"succes",'books':book}
            else:
                    datos={'message':"producto no encontradas"}  
            return JsonResponse(datos)

