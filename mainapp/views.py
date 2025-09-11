from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 
from .models import Table


def index(request):
    tables = Table.objects.all()
    return render(request, 'mainapp/index.html', {'tables': tables})

def index_m(request):
    return render(request, 'mainapp/index_main.html')