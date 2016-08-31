from django.test import TestCase

from ...models import DataWayCooking


class WayCookingTests(TestCase):
    def test_str(self):
        data_way_cooking = DataWayCooking.objects.create(description='Some description')

        self.assertIsInstance(data_way_cooking, DataWayCooking)
        self.assertEqual(data_way_cooking.description, str(data_way_cooking))
