from django import forms
from cotizaciones.models import Cotizacion
from contactos.models import Contacto

class CotizacionForm(forms.ModelForm):
	contacto = forms.ModelChoiceField(queryset=Contacto.objects.all(), help_text='Contacto: ', \
		required=True, widget=forms.Select(attrs={'class': 'form-control'}))
	monto = forms.FloatField(help_text='Monto: ', \
		required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
	descripcion = forms.CharField(help_text='Descripción: ', \
		required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))

	class Meta:
		model = Cotizacion
		fields = ('contacto', 'monto', 'descripcion',)

class VentaForm(forms.ModelForm):
	monto_total = forms.FloatField(help_text='Monto total: ', \
		required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))

	class Meta:
		model = Venta
		fields = ('monto_total',)