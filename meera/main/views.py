from django.shortcuts import render
import datetime

def index(request):
    today = datetime.datetime.now()

    return render(request, 'index.html', {'today':today})

def thema1(request):
    today = datetime.datetime.now()
    return render(request, 'thema1.html', {'today':today})

def thema1_1(request):
    today = datetime.datetime.now()
    return render(request, 'thema1_1.html', {'today':today})

def thema2(request):
    today = datetime.datetime.now()
    return render(request, 'thema2.html', {'today':today})

def thema3(request):
    today = datetime.datetime.now()
    return render(request, 'thema3.html', {'today':today})

def thema4(request):
    today = datetime.datetime.now()
    return render(request, 'thema4.html', {'today':today})