from TheSparkFoundation.models import Customers
from django.shortcuts import render
from django.http import HttpResponse
from .models import Customers

# Create your views here.
def home(request):
    return render(request,'home.html')
def view(request):
    accs = Customers.objects.all()
    context = {'accs':accs}
    return render(request,'view.html',context)
def customer_details(request,customer_id):
    detail = Customers.objects.get(id=customer_id)
    context = {'details':detail}
    return render(request,'customer_details.html',context)
def transfer(request):
    return render(request,'transfer.html')

