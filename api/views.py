from django.shortcuts import render
from .models import Categorias, Produto
from rest_framework.decorators import api_view
from .serializers import CategoriaSerializer, ProdutoSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def listar_categorias(request):
    if request.method == 'GET':
        # Queryset para pegar algo do import
        queryset = Categorias.objects.all().order_by("id") # O order guarda os nomes em ordem alfabetica
        serializers = CategoriaSerializer(queryset, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = CategoriaSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

@api_view(['GET', 'POST'])
def listar_produtos(request):
    if request.method == 'GET':
            # Queryset para pegar algo do import
            queryset = Produto.objects.all().order_by("id") # O order guarda os nomes em ordem alfabetica
            serializers = ProdutoSerializer(queryset, many=True)
            return Response(serializers.data)
    elif request.method == 'POST':
        serializers = ProdutoSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
