from django import forms
from contactos.models import Contacto, Pertenece, Area, Atiende, Calificacion
from contactos.models import Nota, Recordatorio, Llamada
from contactos.models import NumeroTelefonico, TipoNumeroTelefonico
from empresas.models import Empresa
from principal.models import Vendedor

class ContactoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=35, help_text='Nombre: ', \
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellido = forms.CharField(max_length=35, help_text='Apellido: ', \
        required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all(), \
        help_text='Empresa: ', required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    area = forms.ModelChoiceField(queryset=Area.objects.all(), help_text='Area: ', \
        required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    correo_electronico = forms.EmailField(help_text='Email: ', required=True, \
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    calificacion = forms.ModelChoiceField(help_text='Calificación: ', \
        queryset=Calificacion.objects.all(), required=True, \
        widget=forms.Select(attrs={'class':'form-control'}))
    is_cliente = forms.BooleanField(help_text='Cliente: ', required=False, \
        widget=forms.CheckboxInput(attrs={'class':'form-control'}))

    class Meta:
        model = Contacto
        fields = ('nombre', 'apellido', 'empresa', 'area', 'correo_electronico', \
            'calificacion', 'is_cliente',)

class LlamadaForm(forms.ModelForm):
    contacto = forms.ModelChoiceField(queryset=Contacto.objects.all(), help_text='Contacto: ', \
        required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(help_text='Descripción: ', \
        required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = Contacto
        fields = ('contacto', 'descripcion',)

class NotaForm(forms.ModelForm):
    contacto = forms.ModelChoiceField(queryset=Contacto.objects.all(), help_text='Contacto: ', \
        required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(help_text='Descripción: ', \
        required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    clasificacion = forms.ChoiceField(help_text='Clasificación: ', choices=[(x, x) for x in range(1, 4)], \
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Contacto
        fields = ('contacto', 'descripcion', 'clasificacion',)

class RecordatorioForm(forms.ModelForm):
    contacto = forms.ModelChoiceField(queryset=Contacto.objects.all(), help_text='Contacto: ', \
        required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    descripcion = forms.CharField(help_text='Descripción: ', \
        required=True, widget=forms.Textarea(attrs={'class': 'form-control'}))
    urgencia = forms.ChoiceField(help_text='Urgencia: ', choices=[(x, x) for x in range(1, 4)], \
        widget=forms.Select(attrs={'class': 'form-control'}))
    fecha = forms.DateField(help_text='Fecha y hora: ', \
        widget=forms.DateTimeInput(attrs={'class': 'form-control datepicker'}))

    class Meta:
        model = Recordatorio
        fields = ('contacto', 'descripcion', 'urgencia', 'fecha',)

class AtiendeForm(forms.ModelForm):
    vendedor = forms.ModelChoiceField(queryset=Vendedor.objects.all(), help_text='Vendedor: ', \
        required=True, widget=forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = Atiende
        fields = ('vendedor',)