from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from . models import Product, Customer, Collection, Order, OrderItem
# Create your views here.
def home(request):
    # products = Product.objects.all().filter(unit_price__gte=5)
    # product = Product.objects.filter(pk=1).first()
    # product_exists = Product.objects.filter(pk=1).exists()
    # print(product)
    # print(product_exists)
    # products = Product.objects.filter(unit_price__lte=10).order_by('unit_price')
    # products = Product.objects.filter(unit_price__range=(5,10)).order_by('unit_price')
    # products = Product.objects.filter(collection__id=5).order_by('unit_price')
    # customers = Customer.objects.filter(email__icontains=".com")
    # collection = Collection.objects.filter(featured_product__isnull=False)
    # print(collection)
    # orders = Order.objects.filter(customer__id=1)
    # print(orders)
    # group > category > sub category
    order = OrderItem.objects.filter(product__collection__id=1)
    print(order)
    products = Product.objects.filter(last_update__year=2021).order_by('title')
    try:
        product = Product.objects.get(pk=0)
        print(product)
    except ObjectDoesNotExist as e:
        print(e)
        
    return render(request, 'index.html', {'products': products})