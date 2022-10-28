from cgitb import html
from msilib.schema import ListView
import re
from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Familiar
from AppCoder.forms import Buscar, FamiliarForm
from django.views import View 


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


def mostrar_familiares(request):
    lista_familiares = Familiar.objects.all()        #obtenemos los familiares de la base de datos.
    return render(request, "Appcoder/familiares.html", 
    {"lista_familiares": lista_familiares})

class BuscarFamiliar(View):

    form_class = Buscar
    template_name = 'AppCoder/buscar.html'
    initial = {"nombre":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all() 
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})

class AltaFamiliar(View):

    form_class = FamiliarForm
    template_name = 'AppCoder/alta_familiar.html'
    initial = {"nombre":"", "direccion":"", "numero_pasaporte":""}

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 
                                                        'msg_exito': msg_exito})
        
        return render(request, self.template_name, {"form": form})

class FamiliarList(ListView):
    model = Familiar
