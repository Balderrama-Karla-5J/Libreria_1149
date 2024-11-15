from django.db import models

# Create your models here.
class Libros(models.Model):
    Id_libro = models.CharField(primary_key=True,max_length=6)
    Titulo = models.CharField(max_length=200)
    Autor = models.CharField(max_length=150)
    Ilustrador = models.CharField(max_length=150)
    Año_de_salida = models.DateField()
    Precio = models.FloatField()
    Stock = models.IntegerField()

    def __str__(self):
        return self.Titulo
