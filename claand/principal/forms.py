from django import forms
from principal.models import Vendedor

class VendedorForm(forms.ModelForm):
	nombre = forms.CharField(help_text='Nombre: ', \
		required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
	apellido = forms.CharField(help_text='Apellido: ', \
		required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
	contacto = forms.ModelChoiceField(queryset=Contacto.objects.all(), help_text='Contacto: ', \
		required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	monto = forms.FloatField(help_text='Monto: ', \
		required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
	

	class Meta:
		model = Cotizacion
		fields = ('contacto', 'monto', 'descripcion',)

class VentaForm(forms.ModelForm):
	monto_total = forms.FloatField(help_text='Monto total: ', \
		required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Venta
		fields = ('monto_total',)

class PagoForm(forms.ModelForm):
	monto = forms.FloatField(help_text='Monto total: ', \
		required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Pago
		fields = ('monto',)