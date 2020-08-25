from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import GetBooksList, detail, get_books

urlpatterns = [
    path('books/', GetBooksList.as_view(template_name='books/books_list.html'), name='books_list'),
    path('books/<book_id>', detail, name='detail'),
    path('db/', get_books, name='get_books')
]
