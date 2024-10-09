from django.contrib import admin
from .models import LibrosDb

# Register your models here.

admin.site.site_header= "Libreria - Karla Balderrama"
admin.site.index_title= "Libreria"
admin.site.site_title = ""
class LibroAdmin(admin.ModelAdmin):    
    fields = ["titulo", "autor", "ilustrador", "año_salida", "precio", "stock"]
    list_display =["titulo", "autor"]

admin.site.register(LibrosDb, LibroAdmin)