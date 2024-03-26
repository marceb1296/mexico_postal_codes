from django.db import models

# Create your models here.


class PostalCode(models.Model):
    d_codigo = models.CharField(
        max_length=100, verbose_name='Código Postal asentamiento')
    d_asenta = models.CharField(
        max_length=100, verbose_name='Nombre asentamiento')
    d_tipo_asenta = models.CharField(
        max_length=100, verbose_name='Tipo de asentamiento')
    D_mnpio = models.CharField(max_length=100, verbose_name='Nombre Municipio')
    d_estado = models.CharField(max_length=100, verbose_name='Nombre Entidad')
    d_ciudad = models.CharField(max_length=100, verbose_name='Nombre Ciudad')
    d_CP = models.CharField(
        max_length=100, verbose_name='Código Postal Administración Postal')
    c_estado = models.CharField(max_length=100, verbose_name='Clave Entidad')
    c_oficina = models.CharField(
        max_length=100, verbose_name='Código Postal Administración Postal')
    c_CP = models.CharField(max_length=100, verbose_name='Campo Vacio')
    c_tipo_asenta = models.CharField(
        max_length=100, verbose_name='Clave Tipo de asentamiento')
    c_mnpio = models.CharField(max_length=100, verbose_name='Clave Municipio')
    id_asenta_cpcons = models.CharField(
        max_length=100, verbose_name='Identificador único del asentamiento')
    d_zona = models.CharField(
        max_length=100, verbose_name='Zona del asentamiento')
    c_cve_ciudad = models.CharField(
        max_length=100, verbose_name='Clave Ciudad')

    def __str__(self):
        return self.d_codigo

    class Meta:
        ordering = ["pk", ]
