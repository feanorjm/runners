from django import forms

from main.models import Carrera, Corredor, Categoria, Distancia

class CarreraForm(forms.ModelForm):
    class Meta:
        model = Carrera
        fields = ['nombre','fecha']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}),
            'fecha': forms.DateInput(attrs={'id': 'birthday', 'class': 'date-picker form-control col-md-7 col-xs-12"'}),
        }

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['carrera','nombre','edad_ini','edad_fin','sexo']
        widgets = {
            'carrera': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}),
            'edad_ini': forms.TextInput(attrs={'class': 'form-control ', 'pattern': '[0-9]*'}),
            'edad_fin': forms.TextInput(attrs={'class': 'form-control ', 'pattern': '[0-9]*'}),
            'sexo': forms.Select(attrs={'class': 'form-control'}),
        }

class DistanciaForm(forms.ModelForm):
    class Meta:
        model = Distancia
        fields = ['carrera','nombre','distancia']
        widgets = {
            'carrera': forms.Select(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control col-md-7 col-xs-12'}),
            'distancia': forms.TextInput(attrs={'class': 'form-control ', 'pattern': '[0-9]*'})
        }

class CorredorForm(forms.ModelForm):
    class Meta:
        model = Corredor
        fields = ['rut','nombre','apellido_pat','apellido_mat','talla_polera','correo',
                  'ciudad','pais','telefono','team','medicamentos','alergias']
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_pat': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_mat': forms.TextInput(attrs={'class': 'form-control'}),
            'talla_polera': forms.Select(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control ', 'pattern': '[0-9]*'}),
            'team': forms.TextInput(attrs={'class': 'form-control'}),
            'medicamentos': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 90px;'}),
            'alergias': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 90px;'}),
        }