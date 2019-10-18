from django.shortcuts import render
from .models import Processo

def processo_resumo(request):
    total = Processo.objects.count()
    return render(request, 'app_processo/resumo.html', {'total': total})

def lista_processo(request):
    numero = Processo.numero
    funcionario = Processo.funcionario
    data_criacao = Processo.data_criacao