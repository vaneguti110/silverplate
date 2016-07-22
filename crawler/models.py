from django.db import models

# Create your models here.
class Dados_Ingrediente(models.Model):
	Ingrediente = models.CharField(max_length=500)
	Receita = models.CharField(max_length=500)

	def __str__(self):
		return self.descricao