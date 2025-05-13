from .models import ContactInfoHad, Logo, Contacts


def common_context(request):
    info_contact = ContactInfoHad.objects.first()
    logo_main = Logo.objects.first()
    contacts_footer = Contacts.objects.first()
    return {
        'info_contact': info_contact,
        'logo_main': logo_main,
        'contacts_footer': contacts_footer,
    }
