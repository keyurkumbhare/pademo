from django.shortcuts import render


def index(request):
    return render(request, 'demoapp/index.html')
