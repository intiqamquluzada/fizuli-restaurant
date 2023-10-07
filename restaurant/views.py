from django.shortcuts import render
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from restaurant.models import AboutModel, Personal, Service, Menu, Contact, HomeHeader, Category
from restaurant.forms import ContactForm, ReserveForm
from django.contrib import messages
import json


def home_view(request):
    about = AboutModel.objects.first()
    workers = Personal.objects.order_by("-created_at")[:4]
    home_header = HomeHeader.objects.first()
    categories = Category.objects.order_by("name")
    menu_1 = Menu.objects.all()
    cat = request.POST.get("cat_id")
    if cat == '1':
        menu_1 = Menu.objects.filter(category__id=cat)
        print(menu_1)
    

    context = {
        "index_about": about,
        "index_workers": workers,
        "home_header": home_header,
        "categories": categories,
        "menu_1": menu_1,
    }
    return render(request, "index.html", context)


def about_view(request):
    context = {}
    return render(request, "about.html", context)


def service_view(request):
    services = Service.objects.order_by("-created_at")
    context = {
        "services": services,
    }
    return render(request, "service.html", context)


def menu_view(request):
    foods = Menu.objects.order_by("-created_at")
    categories = Category.objects.order_by("name")
    cat_name = request.GET.get("category")

    if cat_name:
        foods = foods.filter(category__name=cat_name)

    paginator = Paginator(foods, 1)
    page = request.GET.get('page', 1)
    p = paginator.get_page(page)
    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)
    context = {
        "foods": foods,
        "categories": categories,
        "p": p,
        "category": cat_name,
    }
    return render(request, "menu.html", context)


def contact_view(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            form = ContactForm()

    else:
        form = ContactForm()

    context = {
        "form": form,
    }
    return render(request, "contact.html", context)


def booking_view(request):
    form = ReserveForm()
    if request.method == "POST":
        form = ReserveForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request,"Məlumatlar göndərildi")
            form = ReserveForm()
        else:

            messages.error(request, "Telefon yalnisdir")

    context = {
        "form": form,
    }
    return render(request, "booking.html", context)


def our_team(request):
    context = {}
    return render(request, "team.html", context)
