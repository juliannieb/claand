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
                try:
                    user.vendedor
                    return HttpResponseRedirect('/principal/vendedor/')
                except Exception:
                    return HttpResponseRedirect('/principal/director/')
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
def vendedor_index(request):
	""" Funcion para manejar el index principal del vendedor.
	TO DO: implementar todo ja.
	"""
	return render(request, 'principal/index_vendedor.html')

@login_required
def consultar(request):
	""" Funcion para manejar la vista principal de consultas.
	TO DO: implementar todo ja.
	"""
	return render(request, 'principal/consultar.html')

@login_required
@user_passes_test(no_es_vendedor)
def director_index(request):
	""" Funcion para manejar el index principal del director.
	Aqui deben ir los permisos de login para el director.
	TO DO: implementar todo ja.
	"""
	return render(request, 'principal/index_director.html')


