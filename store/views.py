from django.shortcuts import render
from .models import models
from django.http import HttpResponse
from .models import Product
# Create your views here.
def products(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'index.html')