from django.db import models

class Jogo(models.Model):
    nome = models.CharField(max_length=100) #MÁXIMO DE DIGITOS NO NOME DO JOGO
    preco = models.DecimalField(max_digits=7, decimal_places=2) #MÁXIMO DE DIGITOS

    def __str__(self):
        return self.nome

class Loja(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.DecimalField(max_digits=15, decimal_places=2)

