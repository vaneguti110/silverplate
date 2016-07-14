from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Ingrediente(models.Model):
	descricao = models.CharField(max_length=150)
	imagem = models.CharField(max_length=500)
	caloria = models.DecimalField(max_digits=5,decimal_places=2)

	def __str__(self):
		return self.descricao


class Usuario(models.Model):
	nome = models.CharField(max_length=150)
	imagem = models.CharField(max_length=500)
	senha = models.CharField(max_length=300)
	sexo = models.CharField(max_length=1)

	def __str__(self):
		return self.nome


class Imagem(models.Model):
	descricao = models.CharField(max_length=150)
	url = models.CharField(max_length=500)

	def __str__(self):
		return self.descricao

class Receita(models.Model):
	descricao = models.CharField(max_length=250)
	modo_preparo = models.CharField(max_length=1000)
	ingredientes = models.ManyToManyField(Ingrediente)
	autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	imagens = models.ManyToManyField(Imagem)
	descricao_ingredientes = models.CharField(max_length = 500)
	
	def __str__(self):
		return self.descricao


class Comentario(models.Model):
	autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	mensagem = models.CharField(max_length=300)
	data_hora = models.DateField(default=timezone.now)