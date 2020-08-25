from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.http import Http404
from django_tables2 import RequestConfig
import requests

from .models import Book
from .services import import_books
from .filters import BookFilter, BookFilterFormHelper
from .tables.tables import BookTable

# Create your views here.


class GetBooksList(TemplateView):
    template_name = 'books/books_list.html'

    def get_queryset(self, **kwargs):
        response = requests.get("https://www.googleapis.com/books/v1/volumes?q=Hobbit")
        data = response.json()
        import_books(data['items'])
        book_list = Book.objects.order_by('-published_date')

        return book_list

    def get_context_data(self, **kwargs):
        context = super(GetBooksList, self).get_context_data(**kwargs)
        my_filter = BookFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        has_filter = any(field in self.request.GET for field in set(my_filter.get_fields()))
        my_filter.form.helper = BookFilterFormHelper()
        table = BookTable(my_filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = my_filter
        context['has_filter'] = has_filter
        context['table'] = table

        return context


def detail(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        raise Http404("Book does not exist")
    return render(request, 'books/book_details.html', {'book': book})


def get_books(request):
    response = requests.get('https://www.googleapis.com/books/v1/volumes?q=war')
    data = response.json()
    import_books(data['items'])
    return redirect('/books/')
