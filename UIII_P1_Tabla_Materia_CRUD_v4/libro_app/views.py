from django.shortcuts import render, redirect
from .models import Libros

# Create your views here.
def inicio_vista(request):
    loslibros=Libros.objects.all()
    return render(request,"gestionarlibros.html",{"mislibros":loslibros})


def registrarLibro(request):
    Id_libro=request.POST["txtcodigo"]
    Titulo=request.POST["txttitulo"]
    Autor=request.POST["txtautor"]
    Ilustrador=request.POST["txtilustrador"]
    Año_de_salida=request.POST["txtfecha"]
    Precio=request.POST["numprecio"]
    Stock=request.POST["numstock"]

    guardarlibro=Libros.objects.create(
        Id_libro=Id_libro,Titulo=Titulo, Autor=Autor,Ilustrador=Ilustrador,Año_de_salida=Año_de_salida,Precio=Precio
    )
    return redirect("/")

