from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def store(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "store/store.html", context)

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {"product": product}
    return render(request, "store/product.html", context)

@login_required(login_url="login")
def cart(request):
    user = request.user
    order, created = Order.objects.get_or_create(user=user, complete=False)
    items = order.orderitem_set.all()
    context = {"items": items, "order": order}
    return render(request, "store/cart.html", context)

@login_required(login_url="login")
def checkout(request):
    user = request.user
    order, created = Order.objects.get_or_create(user=user, complete=False)
    items = order.orderitem_set.all()
    context = {"items": items, "order": order}
    return render(request, "store/checkout.html", context)

@login_required(login_url="login")
def updateItem(request):
    data = json.loads(request.body)
    productId = data["productId"]
    action = data["action"]
    
    user = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(user=user, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)
        
    orderItem.save()
    
    if orderItem.quantity <= 0:
        orderItem.delete()
        
    return JsonResponse("Item was added", safe=False)

def login_user(request):
    if request.user.is_authenticated:
        return redirect("store")
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("store")
    else:
        form = AuthenticationForm()
        
    context = {"form": form}
    return render(request, "store/login.html", context)

def logout_user(request):
    logout(request)
    return redirect("login")

def register_user(request):
    if request.user.is_authenticated:
        return redirect("store")
        
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("store")
    else:
        form = UserCreationForm()
        
    context = {"form": form}
    return render(request, "store/register.html", context)

