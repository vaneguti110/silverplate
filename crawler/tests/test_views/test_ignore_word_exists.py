from django.test import TestCase

from ...models import IgnoredWords
from ...views import ignore_word_exists


class IgnoreWordExistsTests(TestCase):
    def test_existed(self):
        IgnoredWords.objects.create(word='word')
        self.assertTrue(ignore_word_exists('word'))

    def test_not_exists(self):
        self.assertFalse(ignore_word_exists('word'))
