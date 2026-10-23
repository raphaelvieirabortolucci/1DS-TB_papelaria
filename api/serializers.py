from rest_framework.serializers import ModelSerializer
from .models import Categorias, Produto


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'


class ProdutoSerializer(ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'
      