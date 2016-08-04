from django.shortcuts import render

from .models import *

def index(request):
	return render(request, 'index.html')

def artistas_listar(request):
	context = {'artistas' : Artista.objects.all() }
	return render(request,'artistas/listar.html', context)