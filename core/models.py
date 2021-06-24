from django.db import models


# Create your models here.

class Hardware(models.Model):
    tipoHardware = models.CharField(max_length=20, verbose_name="Tipo de Hardware")
    nombreHardware = models.CharField(max_length=20, verbose_name="Modelo del Hardware")
    precio = models.IntegerField()
    anio_lanzamiento = models.IntegerField(verbose_name="Año lanzamiento")
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombreHardware


