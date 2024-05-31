from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from app.models import userdata

def land(request):
    return render(request,"land.html")

def purchase(request):
    return render(request,"purchase.html")

def loginpage(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def signupfunct(request):
     if request.method == "POST":
        first_name = request.POST["name"]
        username = request.POST['uname']
        mail=request.POST["mail"]
        password=request.POST["password"]
        vendor=request.POST["vendor"]
        if User.objects.filter(username=username).exists():
            messages.info(request, "This username is already taken")
            return render(request , "signup.html")
        if User.objects.filter(mail=mail).exists():
            messages.info(request, "This mail is already taken")
            return render(request,"signup.html")
        else:
            user = User.objects.create_user(
                first_name=first_name,
                username=username,
                password=password,
                mail=mail,
            )
            user.save()
            userd=user.id
            data=userdata(vendor=vendor, user_id=userd)
            data.save()
            # data2 = trip(tripnumber="TRIP001",user_id=userd)
            # data2.save()
            return redirect("loginpage")

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