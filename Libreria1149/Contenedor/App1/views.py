from django.shortcuts import render
from .models import LibrosDb
#from django.http import HttpResponse


# Create your views here.
def IndexView(request):
    "Esto es la pagina principals"
    obj = LibrosDb.objects.all().order_by("id")
    return render(request, "index.html", {"Objeto":obj})
