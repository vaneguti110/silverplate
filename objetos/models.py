from django.db import models
from datetime import datetime
from django.utils import timezone

class Ingredient(models.Model):
	description = models.CharField(max_length=150)
	image = models.CharField(max_length=500)

	def __str__(self):
		return self.description


class User(models.Model):
	name = models.CharField(max_length=150)
	image = models.CharField(max_length=500)
	password = models.CharField(max_length=300) 
	sex = models.CharField(max_length=1)

	def __str__(self):
		return self.name

class Image(models.Model):
	description = models.CharField(max_length=150)
	url = models.CharField(max_length=500)

	def __str__(self):
		return self.descricao

class Recipe(models.Model):
	LANG=(('EN',"English"),('PT',"Portuguese"))
	language= models.CharField(max_length=10, choices=LANG)
	description = models.CharField(max_length=250)
	step = models.CharField(max_length=1000)
	ingredients = models.ManyToManyField(Ingredient)
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	images = models.ManyToManyField(Image)
	description = models.CharField(max_length=500)
	
	def __str__(self):
		return self.descricao

class Recipe_Ingredient(models.Model):
	ingredient = models.OneToOneField(Ingredient)
	recipe = models.OneToOneField(Recipe)
	description = models.CharField(max_length=500)

class Comment(models.Model):
	creator = models.ForeignKey(User, on_delete=models.CASCADE)
	message = models.CharField(max_length=300)
	date_time = models.DateField(default=timezone.now)
