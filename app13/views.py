from django.shortcuts import render

# Create your views here.
def third(request):
    return render(request,'three.html')
def fourth(request):
    return render(request,'four.html')

