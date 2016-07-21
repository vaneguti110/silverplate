from html.parser import HTMLParser

class LinkFinder(HTMLParser):

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