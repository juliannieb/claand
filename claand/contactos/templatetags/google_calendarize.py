from django import template
from django.contrib.sites.models import Site
from django.utils.http import urlquote_plus

from contactos.models import Recordatorio

register = template.Library()

@register.filter
def google_calendarize(evento):
    st = evento.fecha
    en = evento.fecha and evento.fecha or evento.fecha
    tfmt = '%Y%m%dT000000'

    dates = '%s%s%s' % (st.strftime(tfmt), '%2F', en.strftime(tfmt))
    name = str(evento.contacto) + ": " + urlquote_plus(evento.descripcion)

    s = ('http://www.google.com/calendar/event?action=TEMPLATE&' +
         'text=' + name + '&' +
         'dates=' + dates + '&' +
         'sprop=website:' + urlquote_plus(Site.objects.get_current().domain))

    return s + '&trp=false'

google_calendarize.safe = True