from django.shortcuts import render
from restaurant.models import AboutModel, Personal, Service, Menu


def home_view(request):
    about = AboutModel.objects.first()
    workers = Personal.objects.order_by("-created_at")[:4]
    context = {
        "index_about": about,
        "index_workers": workers,
    }
    return render(request, "index.html", context)


def about_view(request):
    context = {}
    return render(request, "about.html", context)


def service_view(request):
    services = Service.objects.order_by("-created_at")
    context = {
        "services":services,
    }
    return render(request, "service.html", context)


def menu_view(request):
    foods = Menu.objects.order_by("-created_at").filter(category__name='Popular Breakfast')
    context = {
        "foods": foods,
    }
    return render(request, "menu.html", context)