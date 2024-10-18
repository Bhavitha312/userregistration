from django.shortcuts import render
from django.http import HttpResponse
from app2.forms import loginform
from app2.models import user

# Create your views here.
def display(req):
    if req.method=='POST':
        res=loginform(req.POST)
        res.save()
        return HttpResponse('data added successfully')
    
    form=loginform()
    return render(req,'login.html',{'form':form})

def details(req):
    if req.method=='POST':
        name=req.POST['name']
        lastname=req.POST['lastname']
        password=req.POST['password']
        try:
            res=user.objects.get(name=name,lastname=lastname, password=password)
            return HttpResponse('data is there in database db browser')
        except user.DoesNotExist:
            return HttpResponse('check the details')
    form=loginform()
    return render(req,'demo.html',{'form':form})
