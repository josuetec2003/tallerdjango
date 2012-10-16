# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from mapas.models import Ubicacion, UbicacionForm
from django.utils import simplejson

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
	return render_to_response(
		'sistema.html', 
		{'form': form, 'page': 1}, 
		context_instance=RequestContext(request)
	)

def process_logout(request):
	logout(request)
	return HttpResponseRedirect('/')

def agregar_ubicacion(request):
	if request.is_ajax():
		if request.method == 'POST':
			form = UbicacionForm(data=request.POST)
			if form.is_valid():
				u = form.save(commit=False)
				u.user = request.user
				u.save()

				respuesta = {'codigo': 1, 'msg': 'La ubicacion fue guardada'}
				return HttpResponse(simplejson.dumps(respuesta))
			else:
				respuesta = {'codigo': 2, 'msg': 'Faltan datos'}
				return HttpResponse(simplejson.dumps(respuesta))

def mis_ubicaciones(request):
	ubicaciones = Ubicacion.objects.filter(user=request.user)
	return render_to_response(
		'mis_ubicaciones.html',
		{'ubicaciones': ubicaciones, 'page': 2},
		context_instance=RequestContext(request)
	)
