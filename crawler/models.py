from django.db import models

# Create your models here.
'''
Class used to Store Ingredients of the recipes found in the crawling process
'''
class Data_Ingredient(models.Model):
	Ingredient = models.CharField(max_length=1000)
	Recipe = models.CharField(max_length=500)
	Group = models.CharField(max_length=500, default='Ingredientes')

	def __str__(self):
		return self.Ingredient
'''
Class used to Store steps of the recipes found in the crawling process
'''
class Data_Way_Cooking(models.Model):
	Description = models.CharField(max_length=500)
	Recipe = models.CharField(max_length=500)
	Group = models.CharField(max_length=500, default='Modo de Fazer')
	
	def __str__(self):
		return self.Description

'''
Class used to manipulate Ingredients found and change data to data mining and found patterns of ingredients
'''
class Ingredient_Spec(models.Model):
	Word = models.CharField(max_length=500)
	Count = models.IntegerField()
	Type = models.CharField(max_length=1)

'''
Model to store words to ignore from Ingredient Spec
'''
class Ignore_Words(models.Model):
	Word = models.CharField(max_length=500)

