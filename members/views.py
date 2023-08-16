from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Products, Product_details
from django import forms
from django.core.mail import send_mail
from django.db import transaction


# from business_portfolio.members.models import Product_details, Products


# Create your views here.
def members(request):
    templates = loader.get_template('first_test.html')
    return HttpResponse(templates.render())


def login_view(request):
    if request.user.is_authenticated:
        return redirect("/home_page/")
    context = {

    }
    if request.POST:
        username = request.POST['ID']
        password = request.POST['PASSWORD']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next = request.GET.get('my_redirect_field')
            if next:
                return redirect(next)
            return redirect('/home_page/')

        else:
            context['error_msg'] = "Invalid User"
            print('error')

    templates = loader.get_template('login.html')
    return HttpResponse(templates.render(context, request))


def forgot_password(request):
    templates = loader.get_template('forgot_password.html')
    context = {}
    if request.POST:
        email = request.POST.get('email', '')
        print("eeee")
        print(email)
        try:
            user = User.objects.get(email=email)
            print(user)
            print("user")
        except:
            context['error_msg'] = "Invalid Email"
        else:
            print(email)
    return HttpResponse(templates.render(context, request))


@login_required(login_url="/login/")
def home_page(request):
    templates = loader.get_template('home_page.html')
    context = {
    }
    return HttpResponse(templates.render(context, request))


def log_out(request):
    # print("logout")
    logout(request)
    template = loader.get_template('log_out.html')
    context = {
    }
    return redirect('/login/')


@login_required(login_url="/login/")
def master(request):
    u = request.user
    print(u)
    templates = loader.get_template('master.html')
    context = {
        'user': u
    }
    return HttpResponse(templates.render(context, request))


@login_required(login_url="/login/")
def product_list(request):
    product_category_list = Product_details.objects.all().values()
    product_list = Products.objects.all()
    paginator = Paginator(product_list, 5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    if request.POST:
        product_name = request.POST['product_name']
        product_price = request.POST['product_price']
        product_category_id = request.POST['product_category']
        product_description = request.POST['product_description']
        product_image = request.FILES['product_image']
        new_product = Products(product_name=product_name, product_price=product_price
                               , product_category_id=product_category_id, product_description=product_description,
                                product_image=product_image)
        new_product.save()
        return redirect('/product_list/')
    templates = loader.get_template('product_list.html')
    return render(request, 'product_list.html', {'page': page, 'product_list': product_list,
                                                 'product_category_list': product_category_list})


@login_required(login_url="/login/")
def edit_product(request, id):
    product = Products.objects.get(id=id)
    product_category_list = Product_details.objects.all().values()
    if request.POST:
        product.product_name = request.POST['product_name']
        product.product_price = request.POST['product_price']
        product.product_category_id = request.POST['product_category']
        product.product_description = request.POST['product_description']
        print("1")
        if request.FILES['product_image'] != None:
            print("hello")
        a = product.product_image = request.FILES['product_image']
        print(a)
        product.save()
        return redirect('/product_list/')
    templates = loader.get_template('edit_product.html')
    context = {
        'product': product,
        'product_category_list': product_category_list,
    }
    return HttpResponse(templates.render(context, request))


@login_required(login_url="/login/")
def delete_product(request, id):
    product = Products.objects.get(id=id)
    product.delete()

    return redirect('/product_list/')


@login_required(login_url="/login/")
def change_password(request):
    if request.POST:
        user_name = request.user.username
        n_password = request.POST['n_password']
        c_password = request.POST['c_password']
        print(n_password)
        print(c_password)
        if n_password == c_password:
            u = User.objects.get(username=user_name)
            u.set_password(n_password)
            u.save()
            return redirect('/home_page/')

    templates = loader.get_template('change_password.html')
    context = {
    }
    return HttpResponse(templates.render(context, request))
