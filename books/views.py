from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from books.models import Books


# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    model = Books
    template_name = 'books/book_list.html'
    login_url = 'account_login'


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = 'books/book_detail.html'
    model = Books
    permission_required = 'books.special_status'


class SearchView(ListView):
    model = Books
    template_name = 'books/search_result.html'

    def get_queryset(self):
        q = self.request.GET.get('q')
        return Books.objects.filter(Q(title__icontains=q) | Q(title__icontains=q))
