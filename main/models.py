from django.db import models
from smart_selects.db_fields import ChainedForeignKey

class Carrera(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.nombre

SEXO_CHOICES = (
    ('F', 'Femenino'),
    ('M', 'Masculino')
)

class Categoria(models.Model):
    carrera = models.ForeignKey(Carrera)
    nombre = models.CharField(max_length=100)
    edad_ini = models.IntegerField()
    edad_fin = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    def __str__(self):
        return self.nombre

class Distancia(models.Model):
    carrera = models.ForeignKey(Carrera)
    nombre = models.CharField(max_length=100)
    distancia = models.IntegerField()
    hora_inicio = models.TimeField(blank=True, null=True)

    def __str__(self):
        return self.nombre

TALLA_CHOICES = (
    ('xxs', 'XXS'),
    ('xs', 'XS'),
    ('s', 'S'),
    ('m', 'M'),
    ('l', 'L'),
    ('xl', 'XL'),
    ('xxl', 'XXL'),
)

class Corredor(models.Model):
    rut = models.CharField(max_length=20,null=True, blank=True)
    nombre = models.CharField(max_length=50,null=True, blank=True)
    apellido_pat = models.CharField(max_length=50,null=True, blank=True)
    apellido_mat = models.CharField(max_length=50,null=True, blank=True)
    edad = models.IntegerField(null=True, blank=True)
    talla_polera = models.CharField(max_length=3, choices=TALLA_CHOICES,null=True, blank=True)
    correo = models.EmailField(max_length=50,null=True, blank=True)
    ciudad = models.CharField(max_length=50,null=True, blank=True)
    pais = models.CharField(max_length=50,null=True, blank=True)
    telefono = models.IntegerField(null=True, blank=True)
    team = models.CharField(max_length=50, null=True, blank=True)
    medicamentos = models.TextField(max_length=150, null=True, blank=True)
    alergias = models.TextField(max_length=150, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    categoria = models.ForeignKey(Categoria, null=True, blank=True)
    distancia = models.ForeignKey(Distancia, null=True, blank=True)

class TblComuna(models.Model):
    nombre = models.CharField(max_length=20, blank=True, null=True)
    idprovincia = models.ForeignKey('TblProvincia', models.DO_NOTHING, db_column='idProvincia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_comuna'


class TblProvincia(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=23, blank=True, null=True)
    idregion = models.ForeignKey('TblRegion', models.DO_NOTHING, db_column='idRegion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_provincia'


class TblRegion(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    iso_3166_2_cl = models.CharField(db_column='ISO_3166_2_CL', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tbl_region'

class Posicion(models.Model):
    numero = models.IntegerField()
    tiempo = models.CharField(max_length=50)
    id_corredor = models.IntegerField()
    categoria_id = models.IntegerField()
    distancia_id = models.IntegerField()
    team = models.CharField(max_length=100, null=True, blank=True)
    lugar_cat_dis = models.IntegerField()
    lugar_gen = models.IntegerField()












