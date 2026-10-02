from django.shortcuts import render
from .models import Categorias
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def listar_categorias(request):
    if request.method == 'GET':
        queryset = Categorias.objects.all()

# Create your views here.
