from django.db import models

# Create your models here.
class Vendedor(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    apellido = models.CharField('Apellido', max_length=50)

    def __str__(self):
        return str(self.id) + ' - ' + self.nombre + ' - ' + self.apellido
