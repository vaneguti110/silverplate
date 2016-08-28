from django.test import TestCase

from ..data_mining import DataMining
from ..models import IngredientSpec


class DataMiningTests(TestCase):
    def test_empty(self):
        dm = DataMining()
        self.assertEqual(len(dm.words), 0)

    def test_add_one_word_contains_one_word(self):
        dm = DataMining()
        dm.analysis('first')
        self.assertEqual(len(dm.words), 1)

    def test_add_two_same_words_contain_one_word(self):
        dm = DataMining()
        dm.analysis('first')
        dm.analysis('first')
        self.assertEqual(len(dm.words), 1)

    def test_add_two_different_words_contain_two_different_words(self):
        dm = DataMining()
        dm.analysis('first')
        dm.analysis('second')
        self.assertEqual(len(dm.words), 2)

    def test_save_empty_saves_nothing(self):
        dm = DataMining()
        self.assertEqual(len(IngredientSpec.objects.all()), 0)

        dm.save_to_db()
        self.assertEqual(len(IngredientSpec.objects.all()), 0)

    def test_save_one_saves_one(self):
        dm = DataMining()
        self.assertEqual(len(IngredientSpec.objects.all()), 0)

        dm.analysis('first')

        dm.save_to_db()
        self.assertEqual(len(IngredientSpec.objects.all()), 1)
        self.assertEqual(IngredientSpec.objects.first().count, 1)

    def test_save_two_same_saves_one(self):
        dm = DataMining()
        self.assertEqual(len(IngredientSpec.objects.all()), 0)

        dm.analysis('first')
        dm.analysis('first')

        dm.save_to_db()
        self.assertEqual(len(IngredientSpec.objects.all()), 1)
        self.assertEqual(IngredientSpec.objects.first().count, 2)

    def test_save_two_different_saves_two(self):
        dm = DataMining()
        self.assertEqual(len(IngredientSpec.objects.all()), 0)

        dm.analysis('first')
        dm.analysis('second')

        dm.save_to_db()
        self.assertEqual(len(IngredientSpec.objects.all()), 2)
        self.assertEqual(IngredientSpec.objects.first().count, 1)

    def test_was_in_base_append_value(self):
        IngredientSpec.objects.create(word='word', count=1, type='n')

        self.assertEqual(len(IngredientSpec.objects.all()), 1)

        dm = DataMining()
        dm.analysis('word')
        dm.analysis('word')

        dm.save_to_db()
        self.assertEqual(len(IngredientSpec.objects.all()), 1)
        self.assertEqual(IngredientSpec.objects.first().count, 3)





