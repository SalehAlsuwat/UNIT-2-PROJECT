from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect

# Create your views here.

def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/home.html")

def about_poetry_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/about_poetry.html")

def cultural_features_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/cultural_features.html")

def poetry_forms_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/poetry_forms.html")

def poets_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/poets.html")

def about_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/about.html")

def contact_view(request: HttpRequest) -> HttpResponse:
    return render(request, "main/contact.html")

def mode_view(request, mode):

    next_url = request.GET.get("next", "/")

    if mode == "toggle":
        current_mode = request.COOKIES.get("mode", "light")
        mode = "dark" if current_mode == "light" else "light"

    response = redirect(next_url)
    response.set_cookie("mode", mode)

    return response