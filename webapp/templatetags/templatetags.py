# webapp/templatetags/translation_tags.py
import re
import json
import os
from pathlib import Path
from django import template
from django.conf import settings
from django.utils.translation import get_language
from deep_translator import GoogleTranslator
from django.core.cache import cache
from html import unescape

register = template.Library()

# Конфигурация
TRANSLATIONS_DIR = Path(settings.BASE_DIR) / 'translations'
TRANSLATIONS_DIR.mkdir(exist_ok=True)


def get_translation_file(lang: str) -> Path:
    """Получаем путь к файлу переводов для языка"""
    return TRANSLATIONS_DIR / f'{lang}_translations.json'


def load_translations(lang: str) -> dict:
    """Загружаем переводы из JSON файла"""
    file_path = get_translation_file(lang)
    if not file_path.exists():
        return {}

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}


def save_translations(lang: str, data: dict):
    """Сохраняем переводы в JSON файл"""
    file_path = get_translation_file(lang)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def translate_and_cache(text: str, lang: str) -> str:
    """Умный переводчик с кэшированием в JSON и памяти"""
    if text is None:
        return ""

    # Нормализация текста
    clean_text = text.replace('& laquo;', '«').replace('& raquo;', '»').replace('& ndash;', '-')
    clean_text = re.sub(r'(&nbsp;|\s+)', ' ', clean_text).strip()

    # Ключи для кэша
    cache_key = f'trans_{lang}_{hash(clean_text)}'
    json_key = clean_text

    # Проверка кэша
    if cached := cache.get(cache_key):
        return cached

    # Загрузка переводов
    translations = load_translations(lang)
    if json_key in translations:
        cache.set(cache_key, translations[json_key], 86400)
        return translations[json_key]

    # Логика перевода
    try:
        translator = GoogleTranslator(source='auto', target=lang)
        text_to_translate = unescape(clean_text)

        # Обработка длинных текстов
        if len(text_to_translate) > 1000:
            parts = [text_to_translate[i:i + 1000] for i in range(0, len(text_to_translate), 1000)]
            translated = ''.join(translator.translate_batch(parts))
        else:
            translated = translator.translate(text_to_translate)

        # Защита HTML-тегов после перевода
        translated = (
            translated.replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
        )

        # Сохранение результатов
        translations[json_key] = translated
        save_translations(lang, translations)
        cache.set(cache_key, translated, 86400)

        return translated

    except Exception as e:
        print(f'Translation error: {e}')
        return clean_text


@register.simple_tag
def language_prefix(path: str) -> str:
    """Генерация языкового префикса для URL"""
    lang = get_language()
    return f'/{lang}{path}' if lang in ('be', 'en') else path


@register.filter
def translate_text(text: str) -> str:
    """Фильтр для перевода текста с поддержкой HTML"""
    if text is None:
        return ""

    if not isinstance(text, str):
        return text

    current_lang = get_language()

    # Пропуск перевода для русского
    if current_lang == 'ru':
        return text

    # Улучшенное разделение HTML/текста
    parts = re.split(r'(<[^>]+>)', text)
    result = []

    for part in parts:
        if re.match(r'<[^>]+>', part) or part.strip() == '':
            result.append(part)
        else:
            # Защита от None после перевода
            translated = translate_and_cache(part, current_lang) or part
            result.append(translated)

    return ''.join(result)


# Дополнительные функции
def preload_translations(texts: list, langs: list = ['en', 'be']):
    """Пакетная предзагрузка переводов"""
    for lang in langs:
        translations = load_translations(lang)
        need_save = False

        for text in texts:
            clean_text = re.sub(r'(&nbsp;|\s+)', ' ', text).strip()
            if clean_text not in translations:
                try:
                    translator = GoogleTranslator(source='auto', target=lang)
                    translated = translator.translate(clean_text)
                    translations[clean_text] = translated
                    need_save = True
                except Exception as e:
                    print(f'Preload error: {e}')

        if need_save:
            save_translations(lang, translations)


def update_translation_json(lang: str, key: str, value: str):
    """Ручное обновление перевода"""
    translations = load_translations(lang)
    translations[key] = value
    save_translations(lang, translations)
    cache.delete_many([f'trans_{lang}_{hash(k)}' for k in translations.keys()])


def get_all_translations(lang: str) -> dict:
    """Получение всех переводов для языка"""
    return load_translations(lang)


@register.filter
def insert_br_after_n_chars(value, n=28):
    if not value or len(value) <= n:
        return value
    return value[:n] + '<br>' + value[n:]

