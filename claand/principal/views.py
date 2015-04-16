from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.template import RequestContext

def no_es_vendedor(user):
    """Funcion para el decorador user_passes_test
    """
    return not user.groups.filter(name='vendedor').exists()

def user_login(request):
    """ esta vista maneja todo el proceso de login:
    en el caso de que sea un GET, muestra el template de login,
    y si es POST realiza la validacion y redireccionamiento. 
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                es_vendedor = no_es_vendedor(user)
                return HttpResponseRedirect('/principal/index/', {'no_es_vendedor':es_vendedor})
            else:
                return render(request, 'principal/login2.html', {'desactivada':True})
        else:
            return render(request, 'principal/login2.html', {'errors':True})
    else:
        return render(request, 'principal/login2.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/principal/login')

@login_required
def consultar(request):
    """ En esta vista se muestran las opciones de consulta para los usuarios.
    """
    es_vendedor = no_es_vendedor(request.user)
    context = {}
    context['no_es_vendedor'] = es_vendedor
    return render(request, 'principal/consultar.html', context)

@login_required
def index(request):
    """ Vista para mostrar el index del usuario.
    """
    es_vendedor = no_es_vendedor(request.user)
    context = {}
    context['no_es_vendedor'] = es_vendedor
    return render(request, 'principal/index.html', context)
