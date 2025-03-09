# site_app/translation.py
from modeltranslation.translator import register, TranslationOptions
from .models import AboutHistory

@register(AboutHistory)
class AboutHistoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description')