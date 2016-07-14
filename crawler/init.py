from html.parser import HTMLParser
import urllib.request

class MyHTMLParser(HTMLParser):

	links = []


	def handle_starttag(self, tag, attrs):
		if str(tag) == 'a':
			for attr in attrs:
				if attr == 'href':
					for inn in attrs:
						if 'http' in inn:
							print(inn)
							self.links.append(inn)

#Inicialização
response = urllib.request.urlopen('https://www.comidaereceitas.com.br/bolos/bolinho-de-chuva-pratico.html')
html = response.read().decode('utf-8')
parser = MyHTMLParser()
parser.feed(html)