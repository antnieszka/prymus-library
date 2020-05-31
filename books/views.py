from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView, FormView
from django.views.generic import ListView, DetailView

from books.forms import SimpleForm, BookForm
from books.models import Book, Author, Review


def index_page(request):
    return render(request, template_name="index.html")


def book_list(request):
    books = Book.objects.all()
    context = {
        "books": books,
    }
    return render(request, template_name="books/book_list.html", context=context)


def book_details(request, book_id):
    book_from_db = Book.objects.get(id=book_id)
    return render(
        request, template_name="books/book_details.html", context={"book": book_from_db}
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


class UserSignup(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "registration/signup_form.html"


class AuthorList(ListView):
    model = Author
    template_name = "books/author_list.html"


class ReviewList(ListView):
    model = Review


class AuthorDetail(DetailView):
    model = Author
    template_name = "books/author_detail.html"


class ReviewDetail(DetailView):
    model = Review


class SimpleFormView(FormView):
    form_class = SimpleForm
    template_name = "books/simple_form.html"

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        return render(
            request=self.request,
            template_name="books/simple_form_success.html",
            context={"name": name}
        )


class BookCreate(LoginRequiredMixin, CreateView):
    form_class = BookForm
    template_name = "books/book_form.html"


def search(request):
    query = request.GET.get("q")
    if query:
        results = Book.objects.filter(title__icontains=query)
    else:
        results = []
    return render(request, template_name="search_results.html", context={"results": results})
