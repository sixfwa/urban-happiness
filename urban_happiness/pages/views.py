from django.shortcuts import render as _render


def index(request):
    return _render(request, "pages/index.html")


def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]

    return _render(request, "pages/authentication/login.html")