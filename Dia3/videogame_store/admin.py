from django.contrib import admin
from .models import Jogo, Loja

# Register your models here.

class JogoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

admin.site.register(Jogo, JogoAdmin)

class LojaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')

admin.site.register(Loja, LojaAdmin)