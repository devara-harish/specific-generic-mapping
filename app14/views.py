from django.shortcuts import render

# Create your views here.
def first(request):
    return render(request,'one.html')
def second(request):
    return render(request,'two.html')
