from collections import Counter

from .models import IngredientSpec


class DataMining:
    """
    Class responsible for comparing replicated data and storing it in a special model IngredientSpec
    and a group counting repetitions
    """

    def __init__(self):
        self.words = Counter()

    def analysis(self, ingredient):
        self.save_words(ingredient.lower())

    def save_words(self, word):
        self.words[word] += 1

    def save_to_db(self):
        for word, count in self.words.items():
            try:
                ingredient = IngredientSpec.objects.get(word=word)
                ingredient.count += count
                ingredient.save()
            except IngredientSpec.DoesNotExist:
                IngredientSpec.objects.create(word=word, count=count, type='n')
