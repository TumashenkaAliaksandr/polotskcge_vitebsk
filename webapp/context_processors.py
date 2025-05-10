from .models import ContactInfoHad, Logo

def common_context(request):
    info_contact = ContactInfoHad.objects.first()  # Возьмёт первый объект или None
    logo_main = Logo.objects.first()
    return {
        'info_contact': info_contact,
        'logo_main': logo_main,
    }
