'''
Library View Module
'''
from django.views.generic import ListView, DetailView
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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

class BookCreateView(CreateView):
    '''
    Generic class-based view to create new book data
    '''
    model = Book
    template_name = "NewBook.html"
    fields = ("title", "author", "isbn", "description", "price")

    def get_success_url(self):
        return reverse_lazy("bookdetail", kwargs={"pk": self.object.id})


class BookUpdateView(UpdateView):
    '''
    Generic class-based view to create new book data
    '''
    model = Book
    template_name = "NewBook.html"
    fields = ("title", "author", "isbn", "description", "price")

    def get_success_url(self):
        return reverse_lazy("bookdetail", kwargs={"pk": self.object.id})

class BookDeleteView(DeleteView):
    '''
    Book Delete View
    '''
    model = Book
    template_name = "Book_confirm_delete.html"
    success_url = reverse_lazy("bookslist")
