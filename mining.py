from crawler.LinkFinder import LinkFinder
from crawler.DataFinder import IngredienteFinder
from crawler.DataMining import Data_Mining
from crawler.models import Ingrediente_Spec
import urllib.request

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "silverplate.settings")
import django
django.setup()
# your imports, e.g. Django models
from crawler.models import Dados_Ingrediente

Mining = Data_Mining()
ingredientes = Dados_Ingrediente.objects.all()
count = 0
for ingrediente in ingredientes:
	Mining.Analysis(ingrediente.Ingrediente)
	count += 1

for pal in Mining.lista:
	spec = Ingrediente_Spec(Palavra=pal.valor, Count=pal.count, Tipo='n')
	spec.save()









