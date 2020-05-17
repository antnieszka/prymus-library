from django.contrib import admin
from django.urls import path, include

from books import views

urlpatterns = [
    # admin panel on http://127.0.0.1:8000/admin/
    path("admin/", admin.site.urls),

    # user account views
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile/', views.profile_view, name="user_profile"),
    path('accounts/signup/', views.user_signup, name="user_signup"),

    # http://127.0.0.1:8000/
    path("", views.index_page, name="index"),
    # http://127.0.0.1:8000/ksiazki
    # http://127.0.0.1:8000/books
    path("ksiazki", views.book_list, name="book_list"),
    path("books", views.book_list),

    # http://127.0.0.1:8000/ksiazki/314
    path("ksiazki/<int:book_id>", views.book_details, name="book_details"),
]
