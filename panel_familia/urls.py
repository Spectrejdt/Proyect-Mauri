from django.urls import path
from panel_familia.views import FamiliarList, FamiliarCrear, FamiliarBorrar, FamiliarActualizar

urlpatterns=[
    path('', FamiliarList.as_view(), name='familiar-list'),
    path('crear/', FamiliarCrear.as_view(), name= 'familiar-crear'),
    path('<int:pk>/borrar', FamiliarBorrar.as_view(), name='familiar-borrar'),
    path('<int:pk>/actualizar', FamiliarActualizar.as_view(), name='familiar-actualizar'),
]