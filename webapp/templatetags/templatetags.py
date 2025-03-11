from django import template
from django.utils.translation import get_language
from deep_translator import GoogleTranslator
from django.core.cache import cache

register = template.Library()

@register.simple_tag
def language_prefix(path):
    """
    Добавляет префикс текущего языка к пути, если язык не 'ru'.
    Поддерживаемые языки: русский ('ru'), белорусский ('be'), английский ('en').
    """
    current_language = get_language()
    if current_language in ['be', 'en']:
        return f'/{current_language}{path}'
    return path


from django import template
from django.utils.translation import get_language
from deep_translator import GoogleTranslator
from django.core.cache import cache

register = template.Library()

@register.filter
def translate_text(text):
    """
    Переводит текст в зависимости от текущего языка интерфейса.
    Поддерживаемые языки: русский ('ru'), белорусский ('be'), английский ('en').
    Если язык 'ru', перевод не выполняется.
    """
    # Проверяем, является ли текст строкой
    if not isinstance(text, str):
        return text  # Возвращаем оригинальный объект, если это не строка

    current_language = get_language()

    # Поддерживаемые языки
    supported_languages = ['ru', 'be', 'en']

    # Если язык русский или не поддерживается, возвращаем оригинальный текст
    if current_language not in supported_languages or current_language == 'ru':
        return text

    # Удаляем &nbsp из текста перед переводом
    text = text.replace("&nbsp;", "")

    # Ключ для кэша (уникальный для текста и языка)
    cache_key = f"translation_{current_language}_{text}"

    # Проверяем, есть ли перевод в кэше
    cached_translation = cache.get(cache_key)
    if cached_translation:
        return cached_translation

    # Максимальная длина текста для Google Translator (5000 символов)
    max_length = 1000

    try:
        # Если текст длиннее 5000 символов, разбиваем его на части
        if len(text) > max_length:
            chunks = split_text_into_chunks(text, max_length)
            translated_chunks = []

            translator = GoogleTranslator(source='auto', target=current_language)

            # Переводим каждую часть отдельно
            for chunk in chunks:
                try:
                    translated_chunk = translator.translate(chunk)
                    translated_chunks.append(translated_chunk)
                except Exception as e:
                    print(f"Ошибка перевода части текста: {chunk} --> {e}")
                    translated_chunks.append(chunk)  # Возвращаем оригинал части при ошибке

            # Объединяем переведенные части обратно в один текст
            translated_text = ''.join(translated_chunks)
        else:
            # Если текст короче 5000 символов, переводим его напрямую
            translator = GoogleTranslator(source='auto', target=current_language)
            translated_text = translator.translate(text)

        # Сохраняем результат в кэше на 24 часа (86400 секунд)
        cache.set(cache_key, translated_text, timeout=86400)
        return translated_text

    except Exception as e:
        # Логируем ошибку (опционально)
        print(f"Ошибка перевода: {text} --> {e}")
        return text  # Возвращаем оригинальный текст при ошибке


def split_text_into_chunks(text, max_length):
    """
    Разбивает текст на части длиной не более max_length символов.
    Учитывает разбиение по словам для сохранения целостности.
    """
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        # Проверяем, поместится ли слово в текущий кусок
        if sum(len(w) for w in current_chunk) + len(word) + len(current_chunk) <= max_length:
            current_chunk.append(word)
        else:
            # Если текущий кусок заполнен, добавляем его в список и начинаем новый
            chunks.append(' '.join(current_chunk))
            current_chunk = [word]

    # Добавляем последний кусок
    if current_chunk:
        chunks.append(' '.join(current_chunk))

    return chunks
