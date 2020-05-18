from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from books.models import Book


def index_page(request):
    return render(request, template_name="index.html")


def book_list(request):
    books = Book.objects.all()
    context = {
        "klucz": "wartosc",
        "books": books,
    }
    return render(request, template_name="book_list.html", context=context)


def book_details(request, book_id):
    book_from_db = Book.objects.get(id=book_id)
    return render(
        request, template_name="book_details.html", context={"book": book_from_db}
    )

def user_profile(request):
    return render(request, template_name="registration/profile.html")


def user_signup(request):
    if request.method == "POST":
        # zarejestruj użytkownika
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, template_name="registration/signup_complete.html")
        else:
            return render(request, template_name="registration/signup_form.html", context={"form": form})
    else:
        # wyświetl czysty formularz rejestracji
        form = UserCreationForm()

    return render(request, template_name="registration/signup_form.html", context={"form": form})

