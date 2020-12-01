from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ClientForm, SignInForm
from .models import Client


def index_view(request, *args, **kwargs):

    context = {}

    return render(request, "index.html", context)


@login_required(login_url="main:sign_in")
def dashboard_view(request, *args, **kwargs):

    clients_list = Client.objects.all()

    context = {
        "clients_list": clients_list,
    }

    return render(request, "dashboard.html", context)


@login_required(login_url="main:sign_in")
def create_client_view(request, *args, **kwargs):

    if request.method == "POST":
        create_client_form = ClientForm(request.POST)
        if create_client_form.is_valid():
            create_client_form.save()
            create_client_form = ClientForm()

    else:
        create_client_form = ClientForm()

    context = {
        "client_form": create_client_form,
    }

    return render(request, "create_client.html", context)


def sign_in_view(request, *args, **kwargs):
    sign_in_status = False
    if request.user.is_authenticated:
        request.session["sign_in_status"] = True
        return redirect("home")
    else:
        sign_in_form = SignInForm()
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(
                request,
                username=username,
                password=password,
            )

            if user is not None:
                request.session["sign_in_status"] = True
                login(request, user)
                return redirect("main:dashboard")
            else:
                request.session["sign_in_status"] = False
                messages.info(request, "Username or password incorrect!")

        context = {
            "form": sign_in_form,
            "page_heading": "Sign-In",
            "button_value": "Sign-In",
        }

        return render(request, "admin/sign_in.html", context)


@login_required(login_url="main:sign_in")
def sign_out_view(request, *args, **kwargs):
    request.session["sign_in_status"] = False
    logout(request)
    return redirect("main:sign_in")
