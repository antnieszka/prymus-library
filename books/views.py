from django.shortcuts import render

# Create your views here.
from books.models import Book


def hello_world(request):
    return render(request, template_name="hello.html")


def book_list(request):
    books = Book.objects.all()
    context = {
        "klucz": "wartosc",
        "books": books,
    }
    return render(request, template_name="book_list.html", context=context)