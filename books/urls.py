from django.urls import path
from django.views.generic import RedirectView

from .views import GetBooksList, detail, get_books

urlpatterns = [
    path('', RedirectView.as_view(url='/books/')),
    path('books/', GetBooksList.as_view(template_name='books/books_list.html'), name='books_list'),
    path('book/<book_id>', detail, name='detail'),
    path('db/', get_books, name='get_books')
]
