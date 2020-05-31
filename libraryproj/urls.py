from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from books import views

urlpatterns = [
    path("accounts/", include('django.contrib.auth.urls')),
    path("accounts/profile/", views.user_profile, name="user_profile"),
    path("accounts/signup/", views.user_signup, name="user_signup"),

    # admin panel on http://127.0.0.1:8000/admin/
    path("admin/", admin.site.urls),
    # http://127.0.0.1:8000/
    path("", views.index_page, name="index"),
    # http://127.0.0.1:8000/ksiazki
    # http://127.0.0.1:8000/books
    path("ksiazki", views.book_list, name="book_list"),
    path("ksiazki/nowa", views.BookCreate.as_view(), name="book_create"),
    path("books", views.book_list),

    path("autorzy", views.AuthorList.as_view(), name="author_list"),
    path("autorzy/<int:pk>", views.AuthorDetail.as_view(), name="author_detail"),

    path("recenzje", views.ReviewList.as_view(), name="review_list"),
    path("recenzje/<int:pk>", views.ReviewDetail.as_view(), name="review_detail"),

    path("formularz", views.SimpleFormView.as_view()),

    path("wyszukiwanie", views.search, name="search"),

    # http://127.0.0.1:8000/ksiazki/314
    path("ksiazki/<int:book_id>", views.book_details, name="book_details"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
