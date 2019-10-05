from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    nome = models.CharField("Nome: ", max_length=50, null=True)

    def __str__(self):
        return self.nome

class Funcionario(Pessoa):
    matricula = models.CharField("Matricula: ", max_length=20, null=True)

    def __str__(self):
        return self.matricula

class Departamento(models.Model):
    nome = models.CharField("Nome: ",  max_length=80, null=True)

    def __str__(self):
        return self.nome

class Processo(models.Model):
    numero = models.CharField("Número",  max_length=50, null=True)
    data_criacao = models.DateField("Data da Criação:", null=True)
    funcionario = models.ForeignKey(Funcionario, on_delete = models.CASCADE)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    investigado = models.ManyToManyField(Pessoa, related_name='Investigado')
    interessado = models.ManyToManyField(Pessoa, related_name='Iteressado')

    def __str__(self):
        return self.numero

class Tramitacao(models.Model):
    processo = models.ForeignKey(Processo, null=True, blank=True, on_delete=models.SET_NULL)
    origem = models.ForeignKey(Departamento, related_name='Origem', null=True, blank=True, on_delete = models.CASCADE)
    destino = models.ForeignKey(Departamento, related_name='Destino', null=True, blank=True, on_delete = models.CASCADE)

    def __str__(self):
        return self.processo

class Documento(models.Model):
    numero = models.CharField("Número", max_length=50, null=True)
    titulo = models.CharField("Titulo", max_length=50, null=True)
    data = models.DateField("Data:", null=True)
    processo = models.ForeignKey(Processo, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.titulo

class Portaria(Documento):
    nome = models.CharField("Nome: ", max_length=50, null=True)

    def __str__(self):
        return self.nome

class Pedido(Documento):
    justificativa = models.CharField("Justificativa: ", max_length=120, null=True)
    prazo_anterior = models.DateField("Prazo Anterior: ", null=True)
    prazo_novo = models.DateField("Prazo Novo: ", null=True)

    def __str__(self):
        return self.justificativa

class Envio(Documento):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    data_envio = models.DateField("Data de envio:", null=True)

    def __str__(self):
        return self.departamento
