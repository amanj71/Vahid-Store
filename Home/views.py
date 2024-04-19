from django.shortcuts import render, get_object_or_404
from .models import Product, Category, BackgrounFigure
from .forms import ContactForm

# Create your views here.

def home_page(request):
    queryset = Product.objects.exclude(image='').exclude(image=None)
    background = BackgrounFigure.objects.all()
    context = {
        "products": queryset, "background": background,
    }
    return render(request, 'home/home.html', context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        'product': product,
    }
    return render(request, "home/product_detail.html", context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "contact_form": contact_form,
    }
    return render(request, 'home/contact.html', context)

def about_page(request):
    
    context = {

    }
    return render(request, 'home/about.html', context)


