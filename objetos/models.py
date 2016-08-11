from django.db import models
from datetime import datetime
from django.utils import timezone

#Objeto de Ingrediente de pesquisa
class Ingrediente(models.Model):
	descricao = models.CharField(max_length=150)
	imagem = models.CharField(max_length=500)

	def __str__(self):
		return self.descricao


#Objeto de Usuário do site
class Usuario(models.Model):
	nome = models.CharField(max_length=150)
	imagem = models.CharField(max_length=500)
	senha = models.CharField(max_length=300) 
	sexo = models.CharField(max_length=1)

	def __str__(self):
		return self.nome


#Objeto de Imagem do site
class Imagem(models.Model):
	descricao = models.CharField(max_length=150)
	url = models.CharField(max_length=500)

	def __str__(self):
		return self.descricao

#Objeto de receitas 
class Receita(models.Model):
	descricao = models.CharField(max_length=250)
	modo_preparo = models.CharField(max_length=1000)
	ingredientes = models.ManyToManyField(Ingrediente)
	autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	imagens = models.ManyToManyField(Imagem)
	descricao = models.CharField(max_length=500)
	
	def __str__(self):
		return self.descricao

#Objeto de receitas
class Receita_Ingrediente(models.Model):
	ingrediente = models.OneToOneField(Ingrediente)
	receita = models.OneToOneField(Receita)
	descricao = models.CharField(max_length=500)

#Objeto de Comentário das receitas feito por usuário
class Comentario(models.Model):
	autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	mensagem = models.CharField(max_length=300)
	data_hora = models.DateField(default=timezone.now)