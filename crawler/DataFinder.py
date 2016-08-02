from html.parser import HTMLParser

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "silverplate.settings")
import django
django.setup()
# your imports, e.g. Django models
from crawler.models import Dados_Ingrediente

class DataFinder(HTMLParser):
	gravando = 0
	isMainText = 0
	isNomeReceita = 0
	current_receita = ""
	countDivs = 0
	countUl = 0
	ingredientes = 0

	def __init__(self):
		HTMLParser.__init__(self)
		self.ingredientes = 0

	def handle_starttag(self, tag, attrs):
		if str(tag) == 'div':
			if self.procure_class(attrs, 'maintext'):
				self.isMainText = 1
				self.countDivs = 2

		elif str(tag) == 'td':
			if self.procure_class(attrs, 'item contentheading'):
				print('encontrei o nome da receita')
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
		elif str(tag) == 'td' and self.isNomeReceita:
			self.isNomeReceita = 0

	def handle_data(self, data):
		if str(data).strip() != "":
			if self.gravando==1:
				if self.countUl == 1:
					if self.current_receita != "":
						self.ingredientes += 1
						dados = Dados_Ingrediente(Ingrediente=data, Receita=self.current_receita)
						dados.save()
			if self.isNomeReceita:
				self.current_receita = data