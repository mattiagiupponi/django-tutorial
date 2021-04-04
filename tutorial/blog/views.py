
from django.shortcuts import render


def index(request):
    context = {"name": "Primo blog con django"}
    return render(request, 'index.html', context)

