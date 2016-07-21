from LinkFinder import LinkFinder
import urllib.request

#Inicialização
response = urllib.request.urlopen('https://www.comidaereceitas.com.br/bolos/bolinho-de-chuva-pratico.html')
html = response.read().decode('utf-8')
parser = LinkFinder()
parser.feed(html)
acessos = 5
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
print('vai iniciar o processo de coleta de dados')
for link in parser.links:
	response = urllib.request.urlopen(link)
	html = response.read().decode('utf-8')