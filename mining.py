#!/usr/bin/env python
import os
import django

from crawler.DataMining import DataMining
from crawler.models import IngredientSpec, DataIngredient


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "silverplate.settings")

django.setup()
# your imports, e.g. Django models

mining = DataMining()
ingredients = DataIngredient.objects.all()
count = 0
for ingredient in ingredients:
    mining.analysis(ingredient.ingredient)
    count += 1

for pal in mining.words:
    IngredientSpec.objects.create(Word=pal.value.lower(), Count=pal.count, Type='n')
