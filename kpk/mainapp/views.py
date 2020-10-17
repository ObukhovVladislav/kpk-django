from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')
    pass

def catalog(request):
    return render(request, 'mainapp/catalog.html')
    pass

def basket(request):
    return render(request, 'mainapp/basket.html')
    pass