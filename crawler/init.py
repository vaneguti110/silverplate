from html.parser import HTMLParser
import urllib.request

class MyHTMLParser(HTMLParser):

	links = []


	def handle_starttag(self, tag, attrs):
		if str(tag) == 'a':
			for attr in attrs:
				for inn in attr:
					if 'http' in inn and 'comidaereceitas.com' in inn and not 'whatsapp' in inn and not 'facebook' in inn:
						self.push(inn)

	def push(self, link):
		for ilink in self.links:
			if ilink == link:
				return

		self.links.append(link)



#Inicialização
response = urllib.request.urlopen('https://www.comidaereceitas.com.br/bolos/bolinho-de-chuva-pratico.html')
html = response.read().decode('utf-8')
parser = MyHTMLParser()
parser.feed(html)
acessos = 50
i = 0
while acessos > 0:
	link = parser.links[i]
	print(link)
	print('acessos ' + str(acessos))
	response = urllib.request.urlopen(link)
	html = response.read().decode('utf-8')
	parser.feed(html)
	i += 1
	acessos -= 1
	
print('links encontrados' + str(len(parser.links)))