#!/usr/bin/env python
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "silverplate.settings.base")
django.setup()

from crawler.engine import DataMining
from crawler.models import DataIngredient

mining = DataMining()
ingredients = DataIngredient.objects.all()
count = 0
for ingredient in ingredients:
    mining.analysis(ingredient.ingredient)
    count += 1

mining.save_to_db()
