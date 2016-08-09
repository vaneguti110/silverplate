class Palavra():
	valor = ''
	count = 0

	def __init__(self, valor):
		self.valor = valor
		self.count = 1


class Data_Mining():
	lista = set()

	def __init__(self):
		self.lista = set()

	def Analysis(self, ingrediente):
		palavras = ingrediente.split(' ')
		for palavra in palavras:
			self.Salvar_Palavra(palavra)

	def Salvar_Palavra(self, palavra):
		palavra = palavra.replace('.','').replace(',','')
		encontrado = 0
		for p in self.lista:
			if palavra == p.valor:
				p.count += 1
				encontrado = 1

		if not encontrado:
			self.lista.add(Palavra(valor=palavra))


