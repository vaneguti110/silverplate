from django.test import TestCase
from django.test import TestCase
from crawler.LinkFinder import LinkFinder
from crawler.DataFinder import IngredienteFinder
from crawler.models import Dados_Ingrediente
from crawler.DataMining import Data_Mining
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
		link = 'https://www.comidaereceitas.com.br/bolos/bolo-felpudo-de-coco.html'
		response = urllib.request.urlopen(link)
		html = response.read().decode('utf-8')
		finder.feed(html)
		self.assertEqual(12, finder.ingredientes)

	def test_modo_fazer_encontrados(self):
		finder = IngredienteFinder()
		link = 'https://www.comidaereceitas.com.br/bolos/bolo-felpudo-de-coco.html'
		response = urllib.request.urlopen(link)
		html = response.read().decode('utf-8')
		finder.feed(html)
		self.assertEqual(8, finder.passos)

	def test_data_analysis(self):
		mining = Data_Mining()
		mining.Analysis('teste de teste de teste')
		for pal in mining.lista:
			if pal.valor == 'teste':
				self.assertEqual(3, pal.count)
			elif pal.valor == 'de':
				self.assertEqual(2, pal.count)
			print(pal.valor + ' ' + str(pal.count))

		self.assertEqual(2, len(mining.lista))

	def test_filtro_somente_receita(self):
		finder = IngredienteFinder()
		link = 'https://www.comidaereceitas.com.br/informacoes/politica-de-privacidade.html'
		response = urllib.request.urlopen(link)
		html = response.read().decode('utf-8')
		finder.feed(html)
		self.assertEqual(0, finder.ingredientes)