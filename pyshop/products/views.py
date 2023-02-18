from django.shortcuts import render
from django.http import HttpResponse
from .models import Products


def index(request):
    products = Products.objects.all()
    return render(request , 'index.html', {'products': products})

def newproducts(request):
    return HttpResponse('Here New Products')

