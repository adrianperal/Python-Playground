from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    context = {
        'name': 'Adrian',
        'age': 33,
        'nationality': 'ARBRITAESP'
    }
    return render(request, 'index.html', context)
