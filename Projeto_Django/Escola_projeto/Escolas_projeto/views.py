from django.shortcuts import render

def index(request):
#Página principal
    return render(request, 'Escolas_projeto/index.html')
# Create your views here.
