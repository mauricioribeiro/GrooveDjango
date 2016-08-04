from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'index.html', {})

def artistas_listar(request):
	return render(request,'artistas/listar.html')