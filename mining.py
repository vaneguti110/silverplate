#!/usr/bin/env python
import os
import django

from crawler.DataMining import Data_Mining
from crawler.models import IngredientSpec, DataIngredient


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "silverplate.settings")

django.setup()
# your imports, e.g. Django models

Mining = Data_Mining()
ingredients = DataIngredient.objects.all()
count = 0
for ingredient in ingredients:
    Mining.Analysis(ingredient.ingredient)
    count += 1

for pal in Mining.list_words:
    IngredientSpec.objects.create(Word=pal.value.lower(), Count=pal.count, Type='n')
