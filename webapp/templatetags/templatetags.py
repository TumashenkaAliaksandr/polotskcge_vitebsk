from django import template
from django.utils.translation import get_language
from deep_translator import GoogleTranslator

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



# def translate_text(text, src='auto', dest='ru'):
#     translator = GoogleTranslator(source=src, target=dest)
#     return translator.translate(text)

# @register.filter
# def translate_text(text, lang_code='ru'):
#     try:
#         translator = GoogleTranslator(source='auto', target=lang_code)
#         return translator.translate(text)
#     except Exception as e:
#         return text  # Возвращаем исходный текст при ошибке


@register.filter
def translate_text(text):
    """
    Переводит текст в зависимости от текущего языка интерфейса.
    Поддерживаемые языки: русский ('ru'), белорусский ('be'), английский ('en').
    Если язык 'ru', перевод не выполняется.
    """
    current_language = get_language()

    # Поддерживаемые языки
    supported_languages = ['ru', 'be', 'en']

    # Если текущий язык поддерживается и не русский, то переводим
    if current_language in supported_languages and current_language != 'ru':
        try:
            translator = GoogleTranslator(source='auto', target=current_language)
            return translator.translate(text)
        except Exception as e:
            return text  # Возвращаем исходный текст при ошибке
    return text
