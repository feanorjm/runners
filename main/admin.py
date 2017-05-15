from django.contrib import admin
from main.models import Carrera, Categoria, Distancia, Corredor, TblComuna, TblProvincia, TblRegion

class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha')
    list_filter = ['nombre', 'fecha']

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('carrera', 'nombre', 'edad_ini', 'edad_fin', 'sexo')
    list_filter = ['carrera', 'nombre', 'edad_ini', 'edad_fin', 'sexo']

class DistanciaAdmin(admin.ModelAdmin):
    list_display = ('carrera', 'nombre', 'distancia')
    list_filter = ['carrera', 'nombre', 'distancia']

class CorredorAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido_pat','apellido_mat', 'talla_polera',
                    'correo','ciudad', 'pais', 'telefono','team','medicamentos','alergias')
    list_filter = ['ciudad', 'team', 'talla_polera']

class ComunaAdmin(admin.ModelAdmin):
    list_display = ('nombre','idprovincia')
    list_filter = ['nombre','idprovincia']

class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('nombre','idregion')
    list_filter = ['nombre','idregion']

class RegionAdmin(admin.ModelAdmin):
    list_display = ('nombre','iso_3166_2_cl')
    list_filter = ['nombre','iso_3166_2_cl']



admin.site.register(Carrera,CarreraAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Distancia,DistanciaAdmin)
admin.site.register(Corredor,CorredorAdmin)
'''admin.site.register(TblComuna,ComunaAdmin)
admin.site.register(TblProvincia,ProvinciaAdmin)
admin.site.register(TblRegion,RegionAdmin)
'''

