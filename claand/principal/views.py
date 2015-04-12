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
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/principal/vendedor/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Cuenta desactivada")
        else:
            # Bad login details were provided. So we can't log the user in.
            # print "Invalid login details: {0}, {1}".format(username, password)
            return render(request, 'principal/login.html', {'errors':True})

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'principal/login.html', {})

def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/principal/login')

@login_required
def vendedor_index(request):
	""" Funcion para manejar el index principal del vendedor.
	TO DO: implementar todo ja.
	"""
	return render_to_response('principal/index_vendedor.html', context_instance=RequestContext(request))

@login_required
def consultar(request):
	""" Funcion para manejar la vista principal de consultas.
	TO DO: implementar todo ja.
	"""
	return render_to_response('principal/consultar.html', context_instance=RequestContext(request))

@login_required
def director_index(request):
	""" Funcion para manejar el index principal del director.
	Aqui deben ir los permisos de login para el director.
	TO DO: implementar todo ja.
	"""
	return render_to_response('principal/index_director.html', context_instance=RequestContext(request))