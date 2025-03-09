from django import template
from django.utils.translation import get_language

register = template.Library()

@register.simple_tag
def language_prefix(path):
    """
    Этот тег добавляет префикс с текущим языком к пути, если язык не 'en'.
    """
    current_language = get_language()
    if current_language != 'ru':
        return f'/{current_language}{path}'
    return path
