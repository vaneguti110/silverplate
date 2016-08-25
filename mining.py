from crawler.LinkFinder import LinkFinder
from crawler.DataFinder import IngredientFinder
from crawler.DataMining import Data_Mining
from crawler.models import Ingredient_Spec
import urllib.request

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "silverplate.settings")
import django
django.setup()
# your imports, e.g. Django models
from crawler.models import Data_Ingredient

Mining = Data_Mining()
ingredients = Data_Ingredient.objects.all()
count = 0
for ingrediente in ingredients:
	Mining.Analysis(ingrediente.Ingredient)
	count += 1

for pal in Mining.list_words:
	spec = Ingredient_Spec(Word=pal.value.lower(), Count=pal.count, Type='n')
	spec.save()









