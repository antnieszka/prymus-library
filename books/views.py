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
    book_from_database = Book.objects.get(pk=book_id)
    a = 1
    return render(
        request,
        template_name="book_details.html",
        context={"book_in_context": book_from_database},
    )
