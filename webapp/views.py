from django.shortcuts import render


def index(request):
    """Main, center"""

    return render(request, 'webapp/index.html')


def chief_doctor(request):
    """Main Page Doctor Clinic"""

    return render(request, 'webapp/doctors/main_doctor.html')
