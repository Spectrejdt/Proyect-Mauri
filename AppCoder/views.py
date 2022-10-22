from cgitb import html
import re
from django.shortcuts import render
from django.http import HttpResponse

def saludo(request):   #request=peticion
    return HttpResponse("Hola MI primer app")

def saludo_2(request):
    return HttpResponse("Hola MI segundo saludo")

def saludar_a(request,nombre):
    return HttpResponse(f"hola como estas {nombre}")

def mostrar_mi_template (request):
    return render(request, "AppCoder/index.html")

def index(request, nombre, apellido):
    return render(request, "AppCoder/index.html",
    {
        "nombre": nombre,
        "apellido":apellido,
    })

def index_3(request):
    return render (request,"AppCoder/index.html", 
    {"notas": [1,2,3,4,5,6]}

     )

def imc (request, peso, altura):
    
    imc = int(peso)/int(altura)**2
    return render(request,"AppCoder/imc.html", {"imc":imc})
