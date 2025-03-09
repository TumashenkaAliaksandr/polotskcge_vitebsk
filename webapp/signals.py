# signals.py
from django.db.models.signals import pre_save
from django.dispatch import receiver
from translate import Translator
from .models import AboutHistory

translator = Translator(from_lang='auto', to_lang='ru')  # Автоопределение языка оригинала


@receiver(pre_save, sender=AboutHistory)
def auto_translate_fields(sender, instance, **kwargs):
    # Перевод названия
    if not instance.name_ru:
        try:
            instance.name_ru = translator.translate(instance.name)
        except Exception as e:
            print(f"Translation error (name): {e}")
            instance.name_ru = instance.name  # Используем оригинал при ошибке

    # Перевод описания
    if not instance.description_ru:
        try:
            instance.description_ru = translator.translate(instance.description)
        except Exception as e:
            print(f"Translation error (description): {e}")
            instance.description_ru = instance.description
