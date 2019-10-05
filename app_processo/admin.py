from django.contrib import admin
from .models import Pessoa, Funcionario, Departamento, Processo, Tramitacao, Documento, Portaria, Pedido, Envio

admin.site.register(Pessoa)
admin.site.register(Funcionario)
admin.site.register(Departamento)
admin.site.register(Processo)
admin.site.register(Tramitacao)
admin.site.register(Documento)
admin.site.register(Portaria)
admin.site.register(Pedido)
admin.site.register(Envio)
