from django.shortcuts import render
from .models import Product, Category, BackgrounFigure

# Create your views here.

def home_page(request):
    queryset = Product.objects.all()
    context = {
        "products": queryset,
    }
    return render(request, 'home/home.html', context)

def contact_page(request):
    
    context = {

    }
    return render(request, 'home/contact.html', context)

def about_page(request):
    
    context = {

    }
    return render(request, 'home/about.html', context)


