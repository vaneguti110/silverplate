from html.parser import HTMLParser

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "silverplate.settings")
import django
django.setup()
# your imports, e.g. Django models
from crawler.models import Dados_Ingrediente, Dados_Modo_Fazer

class IngredienteFinder(HTMLParser):
	gravando = 0
	isMainText = 0
	isNomeReceita = 0
	current_receita = ""
	countDivs = 0
	countUl = 0
	ingredientes = 0
	passos = 0
	isGrupo = 0
	isFoiModo_de_fazer = 0
	isModo_de_fazer = 0
	grupo = ''

	def __init__(self):
		HTMLParser.__init__(self)
		self.ingredientes = 0

	def handle_starttag(self, tag, attrs):
		if str(tag) == 'div':
			if self.procure_class(attrs, 'maintext'):
				self.isMainText = 1
				self.countDivs = 2
		if str(tag) == 'strong' and self.isMainText:
			self.isGrupo = 1

		elif str(tag) == 'td':
			if self.procure_class(attrs, 'item contentheading'):
				self.isNomeReceita = 1


		elif self.isMainText and str(tag) == 'ul':
			self.gravando = 1
			self.countUl += 1

	def procure_class(self, array, chave):
		for attr in array:
			for inn in attr:
				if str(inn) == chave:
					return 1

	def handle_endtag(self, tag):
		if str(tag) == 'ul' and self.gravando:
			self.gravando = 0
		elif str(tag) == 'div' and self.isMainText:
			self.countDivs -= 1
			if self.countDivs == 0:
				self.isMainText = 0
				self.countUl =  0
		elif str(tag) == 'html':
			self.isModo_de_fazer = 0
		elif str(tag) == 'td' and self.isNomeReceita:
			self.isNomeReceita = 0
		elif str(tag) == 'strong' and self.isGrupo:
			self.isGrupo = 0

	def handle_data(self, data):
		if str(data).strip() != "":
			if self.gravando==1:
				#UL DOS INGREDIENTES
				if self.countUl >= 1 and not self.isModo_de_fazer:
					if self.current_receita != "" and "Receita" in self.current_receita:
						self.ingredientes += 1
						dados = Dados_Ingrediente(Ingrediente=data, Receita=self.current_receita, Grupo=self.grupo)
						dados.save()
				#UL DO MODO DE FAZER
				elif self.isModo_de_fazer:
					if self.current_receita != "":
						self.passos += 1
						dados = Dados_Modo_Fazer(Descricao=data, Receita=self.current_receita, Grupo=self.grupo)
						dados.save()
			if self.isNomeReceita:
				self.current_receita = data
			if self.isGrupo:
				self.grupo = data.strip()
				if self.grupo == 'Modo de preparo':
					self.isModo_de_fazer = 1

