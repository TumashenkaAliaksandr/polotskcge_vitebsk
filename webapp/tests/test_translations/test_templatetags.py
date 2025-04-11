# tests/test_translations.py
from django.test import TestCase

from webapp.templatetags.templatetags import translate_text


class TranslationTests(TestCase):
    def test_translation_flow(self):
        result = translate_text("Тестовый текст")
        self.assertIn(result, ["Test text", "Тэставы тэкст"])

    def test_html_safety(self):
        result = translate_text('<div class="test">Текст</div>')
        self.assertTrue(result.startswith('<div'))
