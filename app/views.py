from django.shortcuts import render

def land(request):
    return render(request,"land.html")

def purchase(request):
    return render(request,"purchase.html")
