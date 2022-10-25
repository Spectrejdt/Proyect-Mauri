from django import forms
from AppCoder.models import Familiar
from django import forms
class Buscar(forms.Form):
      nombre = forms.CharField(max_length=5)   


class FamiliarForm(forms.ModelForm):
  class Meta:                              #meta sirve para dar caracteristicas a un modelo o formulario, es para dar personalizacion
    model = Familiar                       
    fields = ['nombre', 'direccion', 'numero_pasaporte']