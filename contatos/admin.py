from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email',
                    'categoria', 'data_criacao', 'mostrar')

    list_display_links = ('nome', 'sobrenome', 'email',
                          'categoria')

    list_per_page = 10
    search_fields = ('nome', 'sobrenome', 'categoria', 'email', 'telefone')
    list_editable = ('mostrar', 'telefone')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
