from rest_framework import serializers
from .models import Livro, Autor, Cliente, Editora

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = ['nome', 'valor']

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = ['nome', 'email', 'telefone']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nome', 'endereço', 'telefone']

class EditoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Editora
        fields = ['nome', 'email', 'telefone']