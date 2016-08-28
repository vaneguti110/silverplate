from django.test import TestCase

from ...models import DataIngredient


class IngredientTests(TestCase):
    def test_str(self):
        data_ingredient = DataIngredient.objects.create(ingredient='Some description')

        self.assertIsInstance(data_ingredient, DataIngredient)
        self.assertEqual(data_ingredient.ingredient, str(data_ingredient))
