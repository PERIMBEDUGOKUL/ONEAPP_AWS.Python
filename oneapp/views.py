from django.shortcuts import render,redirect
# from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .emails import otp_send
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt

def base(request):
    return render(request,'base.html')

def log_in(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=User.objects.filter(username=username,password=password).first()
        print("hhh", user)
        if user is not None:
            login(request,user)
            return redirect('profile')
        else:
            messages.info(request,'Username or Password invalid')   
    return render(request,'login.html',{})

@login_required(login_url='login')

def profile(request):
    return render(request,'profile.html',{"user":request.user})

def log_out(request):
    logout(request)
    return redirect('login')
    
firstname=''
lastname=''
email=''
otp=''

def registration(request):
    return render(request,'registration.html',{})

def verifyotp(request):
    global firstname,lastname,email,otp
    if request.method=='POST':
        firstname=request.POST.get('first_name')
        lastname=request.POST.get('last_name')
        email=request.POST.get('email')
        otp=otp_send(email)
        return render(request,'next.html',{'email':email})
    else:
        return redirect('regdisp')


def password(request):
    userotp=request.POST.get('otpverif')
    if int(userotp)==otp:
        return render(request,'password.html',{})
    else:
        messages.info(request,'Invalid otp')
        return render(request,'next.html',{})

def userRegister(request):
    if request.method=='POST':
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
            user=User(first_name=firstname,last_name=lastname,email=email,password=password1,username=email,is_staff=True)
            user.save()
            messages.success(request,'Registration successful')
            return redirect('login')
        else:
            messages.info(request,'Password didnot match')
            return render(request,'password.html',{})


# Dummy Rendering 
# def profile_main(request):
#     return render(request,'profile.html')    

def aws(request):
    return render(request,'aws.html')

def vpc(request):
    return render(request,'vpc.html')

def ec2(request):
    return render(request,'ec2.html')

def s3(request):
    return render(request,'s3.html')

def report(request):
    return render(request,'report.html')