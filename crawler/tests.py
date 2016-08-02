from django.test import TestCase
from django.test import TestCase
from crawler.LinkFinder import LinkFinder
from crawler.DataFinder import DataFinder
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
		dataFinder = DataFinder()
		link = 'https://www.comidaereceitas.com.br/bolos/bolinho-de-chuva-pratico.html'
		response = urllib.request.urlopen(link)
		html = response.read().decode('utf-8')
		dataFinder.feed(html)
		self.assertEqual(8, dataFinder.ingredientes)
