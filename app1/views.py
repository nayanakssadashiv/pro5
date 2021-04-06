from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index1(request):
    return HttpResponse("<h1>index1 of app1</h1>")
def rend_app1(request):
    return render(request,"home1.html")
def ulr_data(request,data):
    return HttpResponse(f'<h1>this is the data of {data}</h1>')
def fact_num(request,num):
    res=1
    for i in range(1,int(num)+1):
        res*=i
    return HttpResponse(f'<h1>the factorial of {num} is {res}</h1>')
def add(request,num1,num2):
    try:
        num1=int(num1)
    except:
        num1=float(num1)
    try:
        num2=int(num2)
    except:
        num2=float(num2)
    return HttpResponse(f'the addition of {num1} and {num2} is {num1+num2}')
        