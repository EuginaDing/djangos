from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

# Create your views here.
def index(request):
    dests=Course.objects.all()
    return render(request,'index.html', {"dests": dests})

def add(request): 
    addresult=int(request.POST["num1"])+int(request.POST["num2"])
    return render(request, "result.html", {"result": addresult})