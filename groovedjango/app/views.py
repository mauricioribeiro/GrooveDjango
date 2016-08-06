from django.shortcuts import render

from .models import *

def index(request):
	return render(request, 'index.html')

def artistas_listar(request):
	context = {'artistas' : Artista.objects.all() }
	return render(request,'artistas/listar.html', context)

def artistas_detalhar(request, nome_artista):
	context = {'artista' : Artista.objects.get(nome=nome_artista) }
	return render(request,'artistas/detalhar.html', context)