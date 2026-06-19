from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo