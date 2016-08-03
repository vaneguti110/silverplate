from django.test import TestCase
from django.test import TestCase
from crawler.LinkFinder import LinkFinder
from crawler.DataFinder import IngredienteFinder
from crawler.models import Dados_Ingrediente
import urllib.request

# Create your tests here.
class testCrawler(TestCase):

	def test_links_finder_count(self):
		finder = LinkFinder()
		html = '<html><a href="http://comidaereceitas.com/teste">Link 01</a><span>Span no meio</span><a href="http://comidaereceitas.com/teste2">Link 02</a></html>'
		finder.feed(html)
		self.assertEqual(2, len(finder.links))

	def test_push_sem_duplicado(self):
		finder = LinkFinder()
		finder.push('goku')
		finder.push('vegeta')
		finder.push('goku')
		self.assertEqual(2, len(finder.links))

	def test_ingredientes_encontrados(self):
		finder = IngredienteFinder()
		link = 'https://www.comidaereceitas.com.br/bolos/bolinho-de-chuva-pratico.html'
		response = urllib.request.urlopen(link)
		html = response.read().decode('utf-8')
		finder.feed(html)
		self.assertEqual(8, finder.ingredientes)

	def test_ingredientes_salvos_Banco(self):
		ingredientes_salvos_banco = len(Dados_Ingrediente.objects.all())
		print('quantidade ingredientes : %s' % ingredientes_salvos_banco)

		#Processo data finder
		finder = IngredienteFinder()
		link = 'https://www.comidaereceitas.com.br/bolos/bolinho-de-chuva-pratico.html'
		response = urllib.request.urlopen(link)
		html = response.read().decode('utf-8')
		finder.feed(html)

		#Valida se incluiu somente os encontrados
		ingredientes_salvos_banco += 8
		print('quantidade ingredientes agora : %s' % ingredientes_salvos_banco)
		for ingrediente in Dados_Ingrediente.objects.all():
			self.assertNotEqual(ingrediente.Ingrediente, '')
			self.assertNotEqual(ingrediente.Receita, '')

		self.assertEqual(ingredientes_salvos_banco, len(Dados_Ingrediente.objects.all()))