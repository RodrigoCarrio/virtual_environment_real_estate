from django.db import models
from applications.vendedor.models import Vendedor

# Create your models here.
class Inmueble(models.Model):
    titulo = models.CharField('Titulo', max_length = 60)
    tipo = models.CharField('Tipo', max_length = 20)
    locacion = models.CharField('Locacion', max_length = 100)
    precio = models.PositiveIntegerField('Precio', )
    metros_cuadrados = models.PositiveIntegerField('Metros Cuadrados', )
    habitaciones = models.PositiveSmallIntegerField('Habitaciones', )
    baños = models.PositiveSmallIntegerField('Baños',)
    piscina = models.BooleanField('Piscina',)
    garage = models.BooleanField('Garage',)
    contrato = models.CharField('Contrato', max_length = 10)
    año_construccion = models.CharField('Año Construccion', max_length = 5)
    descripcion = models.CharField('Descripcion', max_length = 500)
    imagen = models.ImageField('Imagen', upload_to=None, height_field=None, width_field=None, max_length=None, blank=True)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' - ' + self.titulo + ' - ' + self.tipo + ' - ' + str(self.precio) + ' - ' + self.locacion + ' - ' + str(self.metros_cuadrados) + ' - ' + str(self.habitaciones) + ' - ' + str(self.baños) + ' - ' + str(self.piscina) + ' - ' + str(self.garage) + ' - ' + self.contrato + ' - ' + self.año_construccion + ' - ' + self.descripcion + ' - ' + self.vendedor.nombre
