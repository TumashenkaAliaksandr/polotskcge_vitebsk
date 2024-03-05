from django.shortcuts import render


def index(request):
    """Main, center"""

    return render(request, 'webapp/index3.html')
