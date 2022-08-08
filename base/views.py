from email import message
from itertools import product
from multiprocessing import context
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from unicodedata import category, name
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Productd,category1,Chatr
from django.db.models import Q
from .forms import ProductForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.


def loginPge(request):
    page='login'
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        code =  request.POST.get('password')
    
        try:
            user = User.objects.get(username=username)
        except:
           ''
        
        user = authenticate(request,username=username,password=code)
        if user is not  None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'user does not exist')
        
    context={'page':page}
    return render(request,'base/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('home')
    
    
def registerPage(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)#freezing it in time
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else :
            messages.error(request,'oops')
    context={'form':form}
    return render(request,'base/login.html',context)
    

def home(request):
    q=request.GET.get('q')
    if request.GET.get('q')!=None:
        products223 = Productd.objects.filter(Q(category__name__icontains=q)
                                             |Q(product_name__icontains=q)) 
        categories = category1.objects.all()
    else:
        products223 = Productd.objects.all() 
        categories = category1.objects.all()
        
    product_count=Productd.objects.all().count()
    context = {'products223':products223,'categories':categories,'product_count':product_count}
    return render(request,'base/home.html',context)

def products(request,pk):
    product = Productd.objects.get(id=pk)
    users = User.objects.all()
    context = {'product':product,'users':users}
    return render(request,'base/products.html',context)

@login_required(login_url='login')
def createProduct(request):
    form = ProductForm()
    context = {'form':form}
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'base/product_form.html',context)



@login_required(login_url='login')
def updateProduct(request,pk):
    product = Productd.objects.get(id=pk)
    form = ProductForm(instance=product)
    context = {'form':form}
    
    if request.user != product.owner:
        return HttpResponse('Get the F out of Here')
        
    
    if request.method == 'POST':
        form = ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'base/product_form.html',context)


@login_required(login_url='login')
def deleteProduct(request,pk):
    product = Productd.objects.get(id=pk)
    
    if request.user != product.owner:
            return HttpResponse('Get the F out of Here')
    
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request,'base/delete_product.html',{'obj':product})

@login_required(login_url='login')
def Chatt(request,pk):
    chad = Productd.objects.get(id=pk)
    chat = chad.chatr_set.all()
    if request.method == 'POST':
            Chatr.objects.create(
                chat_user = request.user,
                chadd = chad,
                body = request.POST.get('body') 
            )
            return redirect('chat',pk = chad.id)
    
    context = {'chat':chat,'chad':chad}
    return render(request,'base/chat.html',context)
    
def deleteMessage(request,pk):
    product = Chatr.objects.get(id=pk)
    
    if request.user != product.chat_user:
            return HttpResponse('Get the F out of Here')
    
    if request.method == 'POST':
        product.delete()
        return redirect('home')
    return render(request,'base/delete_product.html',{'obj':product})


def userProfile(request,pk):
    user = User.objects.get(id=pk)
    prods = user.productd_set.all()
    context = {'user':user,'prods':prods}
    return render(request,'base/profile.html',context)
