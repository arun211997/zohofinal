from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages

def land(request):
    return render(request,"land.html")

def purchase(request):
    return render(request,"purchase.html")

def loginpage(request):
    return render(request,"login.html")

def loginfun(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            request.session['uid']=user.id
            return redirect("land")
           
        else:
            messages.info(request, "Invalid password or Password")
            return redirect("loginpage")
        
def logout(request):
    auth.logout(request)
    return redirect("loginpage")