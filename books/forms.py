from django import forms
from books.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = []


class SimpleForm(forms.Form):
    name = forms.CharField(label="Jak masz na imie?")
