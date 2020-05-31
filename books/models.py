from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(verbose_name="tytuł", max_length=100)
    short_description = models.TextField(verbose_name="opis")
    published_at = models.DateField(verbose_name="data publikacji")
    # !!!
    author = models.ManyToManyField(to="books.Author", verbose_name="autorzy", related_name="books")

    class Meta:
        ordering = ["title"]
        verbose_name = "książka"
        verbose_name_plural = "książki"

    def __str__(self):
        return "Książka: " + self.title

    def get_absolute_url(self):
        return reverse("book_details", args=[self.pk])


class Author(models.Model):
    first_name = models.CharField(verbose_name="imię", max_length=100)
    last_name = models.CharField(verbose_name="nazwisko", max_length=100)
    about = models.TextField(verbose_name="o autorze", blank=True)
    photo = models.ImageField(verbose_name="zdjęcie", blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "autor"
        verbose_name_plural = "autorzy"

    def __str__(self):
        return "Autor: " + self.first_name + " " + self.last_name


class Review(models.Model):
    book = models.ForeignKey(to=Book, verbose_name="recenzowana książka", on_delete=models.CASCADE)
    author = models.CharField(verbose_name="autor recenzji", max_length=250)
    content = models.TextField(verbose_name="treść recenzji")
    is_recommended = models.BooleanField(verbose_name="polecam innym")

    class Meta:
        verbose_name = "recenzja"
        verbose_name_plural = "recenzje"

    def __str__(self):
        return "Recenzja książki: " + self.book.title
