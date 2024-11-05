from django.shortcuts import render,redirect
from .models import materia

def inicio_vista(request):
    lasmaterias=materia.objects.all()
# Create your views here.
    return render(request,'gestionarMaterias.html',{"mismaterias":lasmaterias})



def registrarMateria(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]


    registrarMateria=materia.objects.create(codigo=codigo,nombre=nombre,creditos=creditos)
    

    
    return redirect("/")
