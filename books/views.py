from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

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


def profile_view(request):
    return render(request, template_name="registration/profile.html")


def user_signup(request):
    if request.method == 'POST':
        # tu trzeba przetworzyć dane z formularza
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, template_name="registration/signup_complete.html")
    else:
        # tutaj obsługujemy przypadek kiedy użytkownik pierwszy raz wyświetlił stronę
        form = UserCreationForm()

    # na końcu zwracamy wyrenderowanego HTMLa
    return render(request, template_name="registration/signup_form.html", context={'form': form})