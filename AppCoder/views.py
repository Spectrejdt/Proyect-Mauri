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
