from django.urls import path
from app_processo.views import processo_resumo, lista_processo

urlpatterns = [
    path('', processo_resumo, name='resumo'),
    path('lista-processo', lista_processo, name='lista')
]