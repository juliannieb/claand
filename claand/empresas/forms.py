from django import forms
from empresas.models import Empresa, EmpresaTieneDireccion, TipoRedSocial
from empresas.models import RedSocial, Estado, Municipio, Direccion
from contactos.models import NumeroTelefonico, TipoNumeroTelefonico

class EmpresaForm(forms.ModelForm):
	nombre = forms.CharField(max_length=30, help_text='Nombre: ', required=True, \
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	rfc = forms.RegexField(max_length=13, help_text='RFC: ', regex=r'[a-zA-Z0-9]{13}', \
		required=True, error_message ="Debe contener 13 letras y números", \
		widget=forms.TextInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Empresa
		fields = ('nombre', 'rfc',)

	def clean(self):
		cleaned_data = self.cleaned_data


class DireccionForm(forms.ModelForm):
	direccion = forms.CharField(max_length=100, help_text='Dirección: ', required=True, \
		widget=forms.TextInput(attrs={'class': 'form-control'}))
	estado = forms.ModelChoiceField(queryset=Estado.objects.all(), help_text='Estado: ', \
		required=False, widget=forms.Select(attrs={'class': 'form-control', 'id' : 'id_estado'}))
	municipio = forms.ModelChoiceField(queryset=Municipio.objects.all(), help_text='Municipio: ', \
		required=True, widget=forms.Select(attrs={'class': 'form-control', 'id' : 'id_municipio'}))

	class Meta:
		model = Direccion
		fields = ('estado', 'municipio', 'direccion',)

class NumeroTelefonicoForm(forms.ModelForm):
	numero = forms.IntegerField(help_text='Número: ', required=False, \
		widget=forms.NumberInput(attrs={'class': 'form-control'}))
	tipo_numero = forms.ModelChoiceField(queryset=TipoNumeroTelefonico.objects.all(), \
		help_text='Tipo: ', required=False, widget=forms.Select(attrs={'class': 'form-control'}))

	class Meta:
		model = NumeroTelefonico
		fields = ('numero', 'tipo_numero',)

class RedSocialForm(forms.ModelForm):
	link = forms.URLField(help_text='Link: ', required=False, \
		widget=forms.URLInput(attrs={'class': 'form-control'}))
	tipo_red_social = forms.ModelChoiceField(queryset=TipoRedSocial.objects.all(), \
		help_text='Tipo: ', required=False, widget=forms.Select(attrs={'class': 'form-control'}))

	class Meta:
		model = RedSocial
		fields = ('link', 'tipo_red_social',)