from django import forms
from principal.models import Vendedor

class VendedorForm(forms.ModelForm):
	nombre = forms.CharField(help_text='Nombre: ', \
		required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	apellido = forms.CharField(help_text='Apellido: ', \
		required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	correo_electronico = forms.EmailField(help_text='Email: ', required=True, \
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
	usuario = forms.CharField(help_text='Nombre de usuario: ', \
		required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
	password = forms.CharField(help_text='Contraseña: ', \
		required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
	
	class Meta:
		model = Vendedor
		fields = ('nombre', 'apellido', 'correo_electronico', 'usuario', 'password',)