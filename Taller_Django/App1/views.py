from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import AutorDb, FraseDb
# Create your views here.

def IndexView(request):
    '''Esto es la pagina principal'''
    
    objeto = AutorDb.objects.all().order_by("id")


    return render(request, 'index.html', {
        "objeto": objeto
    })

def AutorView(request, id):
    autor = get_object_or_404(AutorDb, id=id)
    return render(request, 'autor.html', {
        "objeto": autor
    })