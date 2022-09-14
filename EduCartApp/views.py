from django.shortcuts import render, redirect
from .models import ShippingAddress, courses, Tutorials, Product, Order, OrderItem
import datetime
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_control



# Create your views here.

def home(request):
    date = date_time()
    tutorials = Tutorials.objects.all()
    course_details = courses.objects.all()
    return render(request, 'EduCartApp/Home.html',
                  {'course_details': course_details, 'tutorials': tutorials, 'time': date})

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.info(request, 'logged in successfully!!')
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials!!')
            return redirect('/login')

    return render(request, 'EduCartApp/Login.html')


def signup(request):
    date = date_time()
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        conf_password = request.POST.get('conf_password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'username already taken')
            return redirect('/signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'email already taken')
            return redirect('/signup')

        if password != conf_password:
            messages.info(request, 'password did not match')
            return redirect('/signup')

        else:
            user_details = User.objects.create_user(username=username, first_name=fname, last_name=lname, email=email,
                                                    password=password)
            user_details.save()
            messages.info(request, 'you are registered!')
            return redirect('/login')

    return render(request, 'EduCartApp/Signup.html', {'time': date})


def logoutuser(request):
    logout(request)
    request.user=None
    messages.info(request, 'logged out successfully!!')
    return redirect('/')


def mycourses(request):
    date = date_time()
    return render(request, 'EduCartApp/Mycourses.html', {'time': date})


def myprofile(request):
    date = date_time()
    return render(request, 'EduCartApp/My-Profile.html', {'time': date})


def manageAddress(request):
    # date = date_time()  {'time': date}
    return render(request, 'EduCartApp/manage-address.html')

    
# @login_required
def mycart(request):
    date = date_time()
    if request.user.is_authenticated:
        customer = request.user.customer
        order, create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {'get_cart_total': 0, 'shipping': False, 'get_cart_items': 0}
    return render(request, 'EduCartApp/My-Cart.html', {'time': date, 'items': items, 'order': order})


@csrf_exempt
def checkouts(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
    return render(request, 'EduCartApp/checkouts.html', {'items': items, 'order': order})


def product_list(request):
    products = Product.objects.all()
    date = date_time()
    return render(request, 'EduCartApp/Productlist.html', {'products': products, 'shipping': False, 'time': date})


def processOrder(request):
    print('data', request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete = False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        if total == order.get_cart_total:
            order.complete=True
            order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer = customer,
                order = order,
                address = data['shipping']['address'],
                city = data['shipping']['city'],
                state = data['shipping']['state'],
                zipcode = data['shipping']['postalcode'],
                country = data['shipping']['country'],
            )
    else:
        print("User is not logged in..")
    return JsonResponse('Payment successful' , safe=False)


def personalinfo(request):
    date = date_time()
    return render(request, 'EduCartApp/personalinfo.html', {'time': date})



def product_details(request):
    return render(request, 'EduCartApp/Product-Details.html')

@csrf_exempt
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId'] 
    action = data['action'] 
    # print('Action:', action)
    # print('ProductId:', productId)

    customer = request.user.customer
    product= Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action=='add':
        orderItem.quantity = (orderItem.quantity + 1)
        # messages.info('Product added to the cart')
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)



# ****************************************************************************************
# date time fucntion
def date_time():
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    msg = 'Good'
    if h < 12:
        msg = msg + ' Morning. '
    elif h < 16:
        msg = msg + ' After Noon. '
    elif h < 21:
        msg = msg + ' Evening. '
    else:
        msg = msg + ' Night. '
    return {'msg': msg, 'date': date}


def view(request):
    tutorials = Tutorials.objects.all()
    return render(request, 'EduCartApp/delete.html', {'tutorials': tutorials})


def delete(request, id):
    tutorials = OrderItem.objects.get(pk=id)
    tutorials.delete()
    return redirect('/mycart')
