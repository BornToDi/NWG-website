from django.shortcuts import render

# Create your views here.
def indexpage(request):
    return render(request, 'index.html')

def contactpage(request):
    return render(request, 'contact.html')

def teampage(request):
    return render(request, 'team.html')

def productpage(request):
    return render(request, 'productsDetails.html')

def jobpostpage(request):
    return render(request, 'post.html')

def jobpage(request):
    return render(request, 'alljob.html')

def allproductpage(request):
    return render(request, 'product.html')
