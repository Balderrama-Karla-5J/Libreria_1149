from django.db import models

# Create your models here.
class LibrosDb(models.Model):
    titulo = models.CharField(max_length=300, verbose_name="Titulo", blank=False)
    autor = models.CharField(max_length=200, verbose_name="Autor")
    ilustrador = models.CharField(max_length=200, verbose_name="Ilustrador")
    año_salida = models.DateField(verbose_name="Año de salida", null=False)
    precio = models.FloatField(verbose_name="Precio", null=False)
    stock= models.IntegerField(verbose_name="Stock", null=False, blank=False)

    class Meta:
        db_table = "Libros"
        verbose_name = "Libro"
        verbose_name_plural= "Libros"

    def __str__(self) -> str:
        return self.titulo
    