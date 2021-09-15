
from django.shortcuts import redirect,render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def loginview(request):
    if request.method=='POST':
         u=request.POST.get('un')
         p=request.POST.get('pw')
         print(u,p)
         user=authenticate(username=u,password=p)

         if user is not None:
             print('valid credentials')
             print('actual Logincode')
             login(request,user)
             return redirect('showorder')
         else:
             print('valid credentials')
             messages.error(request,'invalid credentials')
    template_name='login.html'
    context={}
    return render(request,template_name,context)


             

def registerview(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    template_name='register.html'
    context={'form':form}
    return render(request,template_name,context)

def logoutview(request):
    logout(request)
    return redirect('login')

def changepassview(request):
    if request.method=='POST':
        u=request.POST.get('uname')
        p=request.POST.get('password')
        
        new=request.POST.get('new_pass')
        con=request.POST.get('con_pass')   
        user=authenticate(username=u,password=p)
        if user and new==con:
            usr=User.objects.get(username=u)
            co=str(con)
            usr.set_password(co)
            usr.save()
            return redirect('LOGIN')
        else:
            messages.error(request,"please enter valid credentials")  

    template_name="change.html"
    context={}
    return render(request,template_name,context)  

