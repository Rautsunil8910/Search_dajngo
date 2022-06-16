from django.db.models import query
from django.shortcuts import render

from app.models import Product

# Create your views here.
def search_product(request):
    '''search function'''
    if request.method == "POST":
        query_name = request.POST.get('name' ,None)
        if query_name:
            resutls = Product.objects.filter(name__contains = query_name)
            return render(request,'index.html',{'result':resutls})
    return render(request,'index.html')

