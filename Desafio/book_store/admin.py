from django.contrib import admin
from .models import Livro, Autor, Cliente, Editora

class LivrosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor')

admin.site.register(Livro, LivrosAdmin)

class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')

admin.site.register(Autor, AutorAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereço', 'telefone')

admin.site.register(Cliente, ClienteAdmin)

class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')

admin.site.register(Editora, EditoraAdmin)