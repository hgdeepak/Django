'''
Library View Module
'''
from django.views.generic import ListView, DetailView
from .models import Book

# Create your views here.
class BookListView(ListView):
    '''
    Book List View
    '''
    model = Book
    template_name = "BookList.html"
    context_object_name = "books"

class BookDetailView(DetailView):
    '''
    Book Detail View
    '''
    model = Book
    template_name = "BookDetail.html"
    context_object_name = "book"
