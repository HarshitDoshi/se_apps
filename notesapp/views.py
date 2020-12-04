from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Note
from .forms import NoteForm, SignInForm


def index_view(request, *args, **kwargs):

    context = {}

    return render(request, "index.html", context)


@login_required(login_url="notesapp:sign_in")
def dashboard_view(request, *args, **kwargs):

    current_user = request.user
    notes_list = Note.objects.filter(note_user=current_user)

    context = {
        "notes_list": notes_list,
    }

    return render(request, "utilities/read.html", context)


@login_required(login_url="notesapp:sign_in")
def create_note_view(request, *args, **kwargs):

    if request.method == "POST":
        create_note_form = NoteForm(request.POST)
        if create_note_form.is_valid():
            cleaned_data = create_note_form.cleaned_data["note_title"]
            created_note = Note(note_title=cleaned_data)
            created_note.save()
            # create_note_form.save()
            create_note_form = NoteForm()

    else:
        create_note_form = NoteForm()

    context = {
        "note_form": create_note_form,
    }

    return render(request, "utilities/create.html", context)


def sign_in_view(request, *args, **kwargs):
    request.session["sign_in_status"] = True
    if request.user.is_authenticated:
        request.session["sign_in_status"] = True
        return redirect("notesapp:home")
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
                return redirect("notesapp:home")
            else:
                request.session["sign_in_status"] = False
                messages.info(request, "Username or password incorrect!")

        context = {
            "form": sign_in_form,
            "page_heading": "Sign-In",
            "button_value": "Sign-In",
        }

        return render(request, "admin/sign_in.html", context)


@login_required(login_url="notesapp:sign_in")
def sign_out_view(request, *args, **kwargs):
    request.session["sign_in_status"] = False
    logout(request)
    return redirect("notesapp:sign_in")
