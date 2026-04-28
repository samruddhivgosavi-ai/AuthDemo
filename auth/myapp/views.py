from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    return HttpResponse("Homepage")

def reg(request):
    return render(request,"reg.html")

def formsave(request):
    if request.method == "POST":
        fn = request.POST["first_name"]
        ln = request.POST["last_name"]
        un = request.POST["username"]
        ps = request.POST["password"]

        u1 = User.objects.create_user(first_name=fn, last_name=ln,username=un,password=ps)
        u1.save()

        return HttpResponse("Registration Done Successfully")
    
    else:
        return  HttpResponse("Failed")

def signin(request):
    return render(request,"signin.html")

def signcheck(request):
    if request.method=="POST":
        un=request.POST["username"]
        ps=request.POST["password"]

        data=authenticate(username=un,password=ps)

        if data:
            return HttpResponse("SignIn Successfully")
        else:
            return HttpResponse("Invalid Credentials")
    else:
        return HttpResponse("Failed")