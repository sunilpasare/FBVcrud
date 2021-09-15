
from .models import Product
from .forms import Productform
from django.shortcuts import redirect,render


def createorderview(request):
    form=Productform()
    if request.method == 'POST':
        form=Productform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showorder')
    template_name='addorder.html'
    context={'form':form}
    return render(request,template_name,context)


def showorderview(request):
   
    order=Product.objects.all()
    template_name='showorder.html'
    context={'order':order}
    return render(request,template_name,context)

def Updateorderview(request,id_form):
    order=Product.objects.get(id=id_form)
    form=Productform(instance=order)
    if request.method=='POST':
        form=Productform(request.POST,instance=order)
        if form.is_valid():
           form.save()
           print('updated')
           return redirect('showorder')

    template_name='addorder.html'
    context={'form':form}
    return render(request,template_name,context)

def deleteorderview(request,id_form):
    order=Product.objects.get(id=id_form)
    order.delete()
    print('deleted')
    return redirect('showorder')




    



