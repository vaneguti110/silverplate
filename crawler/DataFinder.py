from html.parser import HTMLParser

class DataFinder(HTMLParser):
	gravando = 0

	def handle_starttag(self, tag, attrs):
		if str(tag) == 'div':
			for attr in attrs:
				for inn in attr:
					if str(inn)=='ul':
						self.gravando = 1

		if str(tag) == 'ul':
			self.gravando = 1

	def handle_endtag(self, tag):
		if str(tag) == 'ul' and self.gravando == 1:
			self.gravando = 0

	def handle_data(self, data):
		if self.gravando==1:
			print(data)