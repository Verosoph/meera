from django.shortcuts import render
import datetime

def index(request):
    today = datetime.datetime.now()

    return render(request, 'index.html', {'today':today})

def thema1(request):
    return render(request, 'thema1.html')

def thema2(request):
    return render(request, 'thema2.html')

def thema3(request):
    return render(request, 'thema3.html')

def thema4(request):
    return render(request, 'thema4.html')