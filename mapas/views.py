from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from mapas.models import Ubicacion, UbicacionForm

def index(request):
	#return HttpResponse("Hola")
	frmLogin = AuthenticationForm()
	frmRegister = UserCreationForm()

	return render_to_response('index.html', 
		{'frmLogin': frmLogin, 'frmRegister': frmRegister}, 
		context_instance=RequestContext(request))

def process_login(request):
	if request.method == 'POST':
		frmLogin = AuthenticationForm(data=request.POST)
		if frmLogin.is_valid():
			user = authenticate(username=request.POST['username'], 
				                password=request.POST['password'])

			if user is not None:
				if user.is_active:
					login(request, user)
					return HttpResponseRedirect('/sistema/')
	else:
		frmLogin = AuthenticationForm()

	frmRegister = UserCreationForm()
	return render_to_response('index.html', 
		{'frmLogin': frmLogin, 'frmRegister': frmRegister}, 
		context_instance=RequestContext(request))


@login_required()
def sistema(request):
	form = UbicacionForm()
	return render_to_response('sistema.html', {'form': form}, context_instance=RequestContext(request))

def process_logout(request):
	logout(request)
	return HttpResponseRedirect('/')