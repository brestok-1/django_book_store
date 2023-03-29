from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books.models import Books


# Create your views here.
class BookListView(ListView):
    model = Books
    template_name = 'books/book_list.html'


class BookDetailView(DetailView):
    template_name = 'books/book_detail.html'
    model = Books
