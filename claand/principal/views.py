from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                """ Aquí se tiene que validar si es vendedor o director """
                return HttpResponseRedirect('/principal/vendedor/')
            else:
                return render(request, 'principal/login.html', {'desactivada':True})
        else:
            return render(request, 'principal/login.html', {'errors':True})

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        return render(request, 'principal/login.html', {})

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
def director_index(request):
	""" Funcion para manejar el index principal del director.
	Aqui deben ir los permisos de login para el director.
	TO DO: implementar todo ja.
	"""
	return render(request, 'principal/index_director.html')


