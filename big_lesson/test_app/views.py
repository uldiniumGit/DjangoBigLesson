from django.shortcuts import render
from .models import Client


# Create your views here.

def main_view(request):
    client = Client.objects.all()
    return render(request, 'test_app/index.html', context={'client': client})


def show_prices(request):
    return render(request, 'test_app/pricing.html')


def about(request):
    return render(request, 'test_app/about.html')
