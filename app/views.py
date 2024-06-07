from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages
from app.models import userdata, orderno, cpurchase
from datetime import datetime
from django.db.models import Q

def land(request):
    return render(request,"land.html")

def purchase(request):
    purchase=cpurchase.objects.all()
    return render(request,"purchase.html",{'purchase':purchase})

def customer(request):
    user=request.session['uid']
    print(user)
    order=orderno.objects.get(user_id=user)
    return render(request,"customer.html",{'order':order})

def loginpage(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def signupfun(request):
     if request.method == "POST":
        first_name = request.POST["name"]
        username = request.POST["username"]
        mail=request.POST["mail"]
        password=request.POST["password"]
        vendor=request.POST["vendor"]
        if User.objects.filter(username=username).exists():
            messages.info(request, "This username is already taken")
            return render(request , "signup.html")
        if User.objects.filter(email=mail).exists():
            messages.info(request, "This mail is already taken")
            return render(request,"signup.html")
        else:
            user = User.objects.create_user(
                first_name=first_name,
                username=username,
                password=password,
                email=mail,
            )
            user.save()
            userd=user.id
            data=userdata(vendor=vendor, user_id=userd)
            data.save()
            data2 = orderno(ordernumber="PO001",user_id=userd)
            data2.save()
            return redirect("loginpage")

def loginfun(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            request.session['uid']=user.id
            if(user.is_superuser==1):
              return redirect("land")
            else:
              return redirect("customer")
           
        else:
            messages.info(request, "Invalid password or Password")
            return redirect("loginpage")
        
def logout(request):
    auth.logout(request)
    return redirect("loginpage")

def addorder(request):
    if request.method == "POST":
        user=request.session['uid']
        date=request.POST.get("date")
        due=request.POST.get("date")
        vendor=request.POST.get("vendor")
        amount=request.POST.get("amount")
        order=request.POST.get("order")
        select=request.POST.get("select")
        data = cpurchase(date=date,duedate=due,vendor=vendor,order=order,user_id=user,total=amount,status=select,filters=0,Sfilters=0)
        data.save()
        user=request.session['uid']
        ordern=orderno.objects.get(user_id=user)
        ordernum=ordern.ordernumber
        numeric_part = int(ordernum[2:])
        numeric_part += 1
        new_order_number = f'PO{numeric_part:03d}'
        ordern.ordernumber=new_order_number
        ordern.save()
        return redirect("customer")
    
def datefilter(request):
    if request.method == "POST":
        startd = request.POST["start_date"]
        endd = request.POST["end_date"]
        select = request.POST.get("select")
        purchased = cpurchase.objects.all()
        for p in purchased:
            p.filters=0
            p.Sfilters=0
            p.save()

        if select is not None:
            for p in purchased:
                if p.status==select:
                    p.Sfilters=1
                    p.save()
                else:
                    p.Sfilters=0
                    p.save()

        purchased = cpurchase.objects.all()
        if startd:
            for p in purchased:
                if p.date>=startd and p.date<=endd:
                    print(p.date)
                    print(startd)
                    p.filters=1
                    p.save()
                else:
                    p.filters=0
                    p.save()
        fildered = cpurchase.objects.filter(filters=1 ,Sfilters=1)
        return render(request,"purchase.html",{'purchase':fildered})

    
