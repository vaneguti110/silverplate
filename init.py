from crawler.LinkFinder import LinkFinder
from crawler.DataFinder import DataFinder
import urllib.request

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "silverplate.settings")
import django
django.setup()
# your imports, e.g. Django models
from crawler.models import Dados_Ingrediente


#Inicialização - Le Links da pagina
response = urllib.request.urlopen('https://www.comidaereceitas.com.br/bolos/bolinho-de-chuva-pratico.html')
html = response.read().decode('utf-8')
parser = LinkFinder()
parser.feed(html)
parser.push('https://www.comidaereceitas.com.br/bolos/bolinho-de-chuva-pratico.html')

acessos = 
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
	
print('links encontrados : ' + str(len(parser.links)))
print('vai iniciar o processo de coleta de dados')

DataParser = DataFinder()
size = len(parser.links)
for link in parser.links:
	size -= 1
	response = urllib.request.urlopen(link)
	html = response.read().decode('utf-8')
	DataParser.feed(html)
	print('processando o link %s, numero : %s' % (link , str(size)))

print('Encontrei %s ingredientes' % len(DataParser.ingredientes))

for ingrediente in DataParser.ingredientes:
	dado = Dados_Ingrediente(Ingrediente=ingrediente, Receita="")
	dado.save()


'''response = urllib.request.urlopen('https://www.comidaereceitas.com.br/bolos/bolinho-de-chuva-pratico.html')
html = response.read().decode('utf-8')
DataParser.feed(html)'''