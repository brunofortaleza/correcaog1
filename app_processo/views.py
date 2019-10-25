from django.shortcuts import render
from .models import Processo

def processo_resumo(request):
    total = Processo.objects.count()
    return render(request, 'app_processo/resumo.html', {'total': total})

def lista_processo(request):
    processos = Processo.objects.all()
    return render(request, 'app_processo/lista_processo.html', {'processos': processos})

