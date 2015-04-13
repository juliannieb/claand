from django import forms
from empresas.models import Empresa, EmpresaTieneDireccion, TipoRedSocial
from empresas.models import RedSocial, Estado, Municipio, Direccion

class EmpresaForm(forms.ModelForm):
	nombre = forms.CharField(max_length=30, help_text='Nombre: ', widget=forms.TextInput(attrs={'class': 'form-control'}))
	rfc = forms.CharField(max_length=13, help_text='RFC: ', widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Empresa
		fields = ('nombre', 'rfc',)

class DireccionForm(forms.ModelForm):
	direccion = forms.CharField(max_length=100, help_text='Dirección: ')
	estado = forms.ModelChoiceField(queryset=Estado.objects.all(), help_text='Estado')
	municipio = forms.ModelChoiceField(queryset=Municipio.objects.all(), help_text='Municipio')

	class Meta:
		model = Direccion
		fields = ('direccion', 'municipio',)