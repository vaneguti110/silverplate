from html.parser import HTMLParser

class DataFinder(HTMLParser):
	gravando = 0
	isMainText = 0
	countDivs = 0
	countUl = 0
	ingredientes = set()

	def __init__(self):
		HTMLParser.__init__(self)
		self.ingredientes = set()

	def handle_starttag(self, tag, attrs):
		if str(tag) == 'div':
			for attr in attrs:
				for inn in attr:
					if str(inn) == 'maintext':
						self.isMainText = 1
						self.countDivs = 2

		if self.isMainText and str(tag) == 'ul':
			self.gravando = 1
			self.countUl += 1

	def handle_endtag(self, tag):
		if str(tag) == 'ul' and self.gravando:
			self.gravando = 0
		if str(tag) == 'div' and self.isMainText:
			self.countDivs -= 1
			if self.countDivs == 0:
				self.isMainText = 0
				self.countUl =  0

	def handle_data(self, data):
		if str(data).strip() != "":
			if self.gravando==1:
				if self.countUl == 1:
					self.ingredientes.add(data)
				#elif self.countUl == 2:
					#print('Modo de Preparo : ' + data)