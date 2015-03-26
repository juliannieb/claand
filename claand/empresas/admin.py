from django.contrib import admin

from empresas.models import Empresa, RedSocial, Estado, Municipio, Direccion
from empresas.models import TipoRedSocial, EmpresaTieneDireccion

admin.site.register(Empresa)
admin.site.register(TipoRedSocial)
admin.site.register(RedSocial)
admin.site.register(Estado)
admin.site.register(Municipio)
admin.site.register(Direccion)
admin.site.register(EmpresaTieneDireccion)
