from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email',
                    'categoria', 'data_criacao')

    list_display_links = ('nome', 'sobrenome', 'telefone', 'email',
                          'categoria')
    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'categoria', 'email', 'telefone')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
