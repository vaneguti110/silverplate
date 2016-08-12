from django.db import models

# Create your models here.
class Data_Ingredient(models.Model):
	Ingredient = models.CharField(max_length=1000)
	Recipe = models.CharField(max_length=500)
	Group = models.CharField(max_length=500, default='Ingredientes')

	def __str__(self):
		return self.Ingredient

class Data_Way_Cooking(models.Model):
	Description = models.CharField(max_length=500)
	Recipe = models.CharField(max_length=500)
	Group = models.CharField(max_length=500, default='Modo de Fazer')
	
	def __str__(self):
		return self.Description

class Ingredient_Spec(models.Model):
	Word = models.CharField(max_length=500)
	Count = models.IntegerField()
	Type = models.CharField(max_length=1)

class Palavras_Ignorar(models.Model):
	Word = models.CharField(max_length=500)

