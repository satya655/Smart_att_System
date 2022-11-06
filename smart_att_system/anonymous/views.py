
# from unicodedata import name
from django.shortcuts import render
from .models import user_master

# Create your views here.

def register(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        mobile = request.POST['mobile']
        role_name = request.POST['role_name']
        status = '1'
        remark = ''
        ob=user_master.objects.create(name=name,email=email,password=password,mobile=mobile,role_name=role_name,status=status,remark=remark)
        ob.save();
        return render(request,'register.html',{'output':"Register Success"})        
    return render(request,"register.html")

def edit(request):
    if request.method=="POST":
        email=request.POST['email']
        name=request.POST['name']
        mobile=request.POST['mobile']
    try:
        user_master.objectc.filter(email=email).update(mobile=mobile,name=name)
        ob=user_master.objects.all()
        return render(request,'viewdata.html',{'users':ob})
    except Exception as e:
        return render(request,'viewdata.html',{'output':"invalid"+str(e)})    
def viewdata(request):
        if request.method=="POST":
            btn=request.POST['btn']
            email=request.POST['email']
            if btn=="delete":
                try:
                    user_master.objects.filter(email=email).delete()
                    ob=user_master.objects.all()
                    return render(request,'viewdata.html',{'users':ob})
                except Exception as e:
                    return render(request,'viewdata.html',{'output':"invalid"}) 
            if btn=="edit": 
                try:
                    ob=user_master.objects.filter(email=email);

                    return render(request,'edit.html',{'users':ob})
                except Exception as e:
                    return render(request,'viewdata.html',{'output':"invalid"})

        try:
            ob=user_master.objects.all()
            return render(request,'viewdata.html',{'users':ob})
        except Exception as e:
            return render(request,'viewdata.html',{'output':"invalid"})  
        return render(request,'viewdata.html')
    
def index(request):
    return render(request,"index.html")
def login(request):
    if request.method=="POST":
        email=request.POST['email']
        password=request.POST['password']
        try:
            ob=user_master.objects.get(email=email,password=password)
            request.session["name"]=ob.name
            request.session["email"]=ob.email
            if ob.role_name=='admin':
                return render(rquest,'adminhomepage.html',{'output':"valid"})
            elif ob.role_name=='student':
                return render(rquest,'studenthomepage.html',{'output':"valid"})
            elif ob.role_name=='faculty':    
                return render(request,'facultyhomepage.html',{'output':"valid"})
            else:
                return render(request,'login.html',{'output':"invalid"})
        except Exception as e:
            return render(request,'login.html',{'output':"invalid"+str(e)})    
    return render(request,"login.html")
# def register(request):
#     return render(request,"register.html")
def contact(request):
    return render(request,"contact.html")
def gallery(request):
    return render(request,"gallery.html")
def about(request):
    return render(request,"about.html")
    return HttpResponse("<h1>Hello World</h1>")