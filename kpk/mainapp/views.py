from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html')
    pass

def catalog(request):

    pass

def basket(request):

    pass