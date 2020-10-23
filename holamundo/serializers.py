from holamundo.models import Carrera,Paralelo,Estudiante
from rest_framework import serializers

class CarreraSerializer(serializers.ModelSerializer):
    class Meta:
        model=Carrera
        fields = ('nombreCarrera' , 'numeroCiclos' , 'numeroCreditos' , 'codigoCarrera' , 'numeroDocentes')

class ParaleloSerializer(serializers.ModelSerializer):    
    class Meta:
        model=Paralelo
        fields=('carrera' , 'ciclo' , 'nombre' , 'numeroEstudiantes')
class EstudianteSerializer(serializers.ModelSerializer):    
    class Meta:
        model=Estudiante
        fields=('nombre' , 'cedula' , 'direccion' , 'telefono')