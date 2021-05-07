from django.shortcuts import render
from .models import Product
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    products=Product.objects.all()
    params = {'product':products}
    return render(request, 'shop/index.html',params)
