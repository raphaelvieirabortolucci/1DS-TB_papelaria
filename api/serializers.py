from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField
from .models import Categorias, Produto


class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'


class ProdutoSerializer(ModelSerializer):

    # Define o campo valor_total antes da classe Meta pegar todos os campos
    valor_total = SerializerMethodField() # Permite fazer calculos

    class Meta:
        model = Produto
        fields = '__all__'

    def get_valor_total(self, produto):
        total = produto.preco * produto.quantidade
        return format(total, ".2f")

    def validate_preco(self, valor):
        if valor < 0:
            raise ValidationError("O valor do produto deve ser maior que zero!")
        return valor
    
    def validate_quantidade(self, valor):
        if valor < 0:
            raise ValidationError("Digite uma quantidade maior que zero!")
        return valor
    