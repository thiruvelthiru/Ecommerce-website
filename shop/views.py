from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"shop/index.html")
def register(request):
    return render(request,"shop/register.html")
def collections(request):
    return render(request,"shop/collections.html")
def product(request):
    return render(request,"shop/product.html")